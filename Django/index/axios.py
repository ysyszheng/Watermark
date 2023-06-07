from django.http import JsonResponse, HttpResponse
from urllib.parse import urlparse
from django.views.decorators.csrf import csrf_exempt
from .models import Image, User
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
@csrf_exempt
def uploadImage_stegan(request):
    jaccount = request.POST.get('jaccount').strip()
    print(jaccount)
    res = {'key': 1}
    file_img = request.FILES['upload_file']  # 获取文件对象
    file_name = request.FILES['upload_file'].name.strip()
    print(file_name)

    if file_name == "":
        res['key'] = 0


    user = User.objects.filter(jaccount=jaccount)[0]
    img = Image.objects.create(user=user, username=user, photo_name=file_name, photo=file_img)
    img.stegan()
    return HttpResponse(json.dumps(res), content_type="application/json")
