from django.http import JsonResponse, HttpResponse
from urllib.parse import urlparse
from django.views.decorators.csrf import csrf_exempt
from .models import Image, User
import json
import os
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
@csrf_exempt
def uploadImage_stegan(request):
    jaccount = request.POST.get('jaccount').strip()
    print(jaccount)
    res = {'key':1}

    file_img = request.FILES['upload_file']  # 获取文件对象
    file_time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) 
    text = request.POST.get('text').strip()

    user = User.objects.filter(jaccount=jaccount)[0]
    img = Image.objects.create(user=user, username=jaccount, file_time=file_time, photo_input=file_img, text=text)
    img.stegan(text)

    res['stegan_photo'] = img.photo_output

    # img.unstegan()
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def uploadImage_unstegan(request):
    jaccount = request.POST.get('jaccount').strip()
    print(jaccount)
    res = {'key':1}
    try:
        file_img = request.FILES['upload_file']  # 获取文件对象（此处是已经含有隐写信息的图片）
        file_time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) 

        user = User.objects.filter(jaccount=jaccount)[0]
        img = Image.objects.create(user=user, username=jaccount, file_time=file_time, photo_input=file_img)
        img.unstegan()

        res['unstegan_text'] = img.text
    except:
        res['key'] = 0
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def uploadImage_watermark(request):
    jaccount = request.POST.get('jaccount').strip()
    print(jaccount)
    res = {'key':1}

    file_img = request.FILES['upload_file']  # 获取文件对象
    file_time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) 
    text = request.POST.get('text').strip()

    user = User.objects.filter(jaccount=jaccount)[0]
    img = Image.objects.create(user=user, username=jaccount, file_time=file_time, photo_input=file_img, text=text)
    img.watermark(text)

    res['watermark_photo'] = img.photo_output
    return HttpResponse(json.dumps(res), content_type="application/json")


@csrf_exempt
def uploadImage_unwatermark(request):
    jaccount = request.POST.get('jaccount').strip()
    print(jaccount)
    res = {'key':1}
    try:
        file_img = request.FILES['upload_file']  # 获取文件对象（此处是已经含有隐写信息的图片）
        template_img = request.FILES['template_file']
        file_time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) 

        user = User.objects.filter(jaccount=jaccount)[0]
        img = Image.objects.create(user=user, username=jaccount, file_time=file_time, photo_input=file_img, template=template_img)
        img.unwatermark()
        res['unwatermark_photo'] = img.photo_output
    except:
        res['key'] = 0
    return HttpResponse(json.dumps(res), content_type="application/json")