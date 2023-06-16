from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Image
from django.views.decorators.csrf import csrf_exempt
import base64
import requests
import json
import time
import logging
logger = logging.getLogger('network_traffic')
# Create your views here.
@csrf_exempt
def index_view(request):
    print("jaccount login:")
    jaccount_default_flag = User.objects.filter(jaccount='0000')
    if not jaccount_default_flag:
        User.objects.create(jaccount='0000')
        user = User.objects.filter(jaccount='0000')[0]
        Image.objects.create(user=user)

    try:
        
        result_origin = jac(request)
        
        result = result_origin['entities'][0]['name']
        jaccount = result_origin['entities'][0]['account']
        
        jaccount_flag = User.objects.filter(jaccount=jaccount)
        
        if not jaccount_flag:
            
            User.objects.create(user_name=result, jaccount=jaccount)
            user = User.objects.filter(jaccount=jaccount)[0]
            Image.objects.create(user=user, username=result, photo_name="XXX", photo="XXX")
        
        
        user = User.objects.filter(jaccount=jaccount)[0]
        
        # 返回隐写图片
        images = Image.objects.filter(user=user, type="stegan")
        image_set = []

        for image in images:
            tmp = {"id": image.id, 'username': result}
            try:
                tmp['text'] = image.text

                with open(image.photo_input.path, 'rb') as f:
                    image_data = f.read()
                tmp['photo_clean'] = base64.b64encode(image_data).decode('utf-8')

                with open("/root/kyrie/kyrie/web/Watermark/Django/media/" + image.photo_output, 'rb') as g:
                    image_processed_data = g.read()

                tmp['photo_processed'] = image_processed_data
                tmp['photo_processed'] = base64.b64encode(image_processed_data).decode('utf-8')

                tmp['file_time'] = image.file_time
                
                
            except:
                continue
            image_set.append(tmp)
        # 返回水印图片
        images = Image.objects.filter(user=user, type="watermark")
        watermark_set = []
        for image in images:
            tmp = {"id": image.id, 'username': result}
            try:
                tmp['text'] = image.text

                with open(image.photo_input.path, 'rb') as f:
                    image_data = f.read()
                tmp['photo_clean'] = base64.b64encode(image_data).decode('utf-8')

                with open("/root/kyrie/kyrie/web/Watermark/Django/media/" + image.photo_output, 'rb') as g:
                    image_processed_data = g.read()
                    
                tmp['photo_processed'] = image_processed_data
                tmp['photo_processed'] = base64.b64encode(image_processed_data).decode('utf-8')
                
                # tmp['photo_clean'] = image.photo_input.__dict__['name']
                # tmp['photo_processed'] = image.photo_output
                tmp['file_time'] = image.file_time
            except:
                continue
            watermark_set.append(tmp)
        
        print(f"Hello {result}!")
    except:
        result = ''
        jaccount = '0000'
        user = User.objects.filter(jaccount='0000')[0]
        image_set = []
        watermark_set = []
        print(f"Please login!")
        print("except!")
    
    id_info = {
        'name': result,
        'account': jaccount,
        'image_set': image_set,
        'watermark_set': watermark_set,
    }

    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    log_message = f"{current_time} - IP: {request.META['REMOTE_ADDR']}, Method: {request.method}, " \
                f"Path: {request.path}, Jaccount Name: {result}"
    logger.info(log_message)


    # print(image_set)
    return HttpResponse(json.dumps(id_info), content_type="application/json")


@csrf_exempt
def jac(request):
    token = request.session['token']
    access_token = token['access_token']
    requests.packages.urllib3.disable_warnings()
    result = requests.get(f'https://api.sjtu.edu.cn/v1/me/profile?access_token={access_token}', verify=False)
    return result.json()

