from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Image
from django.views.decorators.csrf import csrf_exempt

import requests
import json
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
        
        images = Image.objects.filter(user=user)
        image_set = []

        for image in images:
            tmp = {"id", image.id, 'username', result}
            try:
                tmp['photo_name'] = image.photo_name
                tmp['photo_file'] = image.photo
            except:
                continue
            image_set.append(tmp)
        
        print(f"Hello {result}!")
    except:
        result = ''
        jaccount = '0000'
        user = User.objects.filter(jaccount='0000')[0]
        image_set = []
        print(f"Please login!")
        print("except!")
    
    id_info = {
        'name': result,
        'account': jaccount,
        'image_set': image_set,
    }

    return HttpResponse(json.dumps(id_info), content_type="application/json")


@csrf_exempt
def jac(request):
    token = request.session['token']
    access_token = token['access_token']
    requests.packages.urllib3.disable_warnings()
    result = requests.get(f'https://api.sjtu.edu.cn/v1/me/profile?access_token={access_token}', verify=False)
    return result.json()
