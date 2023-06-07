from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Django.oauth import jaccount
from Django.settings import JACCOUNT_CLIENT_ID
from django.shortcuts import redirect
from authlib.jose import jwt
from authlib.oidc.core import CodeIDToken
from urllib.parse import urlencode

from .models import User, Wallpaper
import json
import requests

@csrf_exempt
def index_view(request):
    print("jaccount login:")
    # jaccount_default_flag = User.objects.filter(jaccount='0000')
    # if not jaccount_default_flag:
    #     User.objects.create(jaccount='0000')
    #     user = User.objects.filter(jaccount='0000')[0]
        # Wallpaper.objects.create(user=user)

    try:
        result_origin = jac(request)
        result = result_origin['entities'][0]['name']
        jaccount = result_origin['entities'][0]['account']
        # jaccount_flag = User.objects.filter(jaccount=jaccount)

        print(f"Hello {result}!")
    except:
        result = ''
        jaccount = '0000'
        print(f"Please login!")
        print("except!")
    
    id_info = {
        'name': result,
        'account': jaccount,
    }
    
    return HttpResponse(json.dumps(id_info), content_type="application/json")


@csrf_exempt
def login(request):
    redirect_uri = request.build_absolute_uri('/authorize')
    return jaccount.authorize_redirect(request, redirect_uri)


@csrf_exempt
def authorize(request):
    token: dict = jaccount.authorize_access_token(request)
    claims = jwt.decode(token.pop('id_token'),
                        jaccount.client_secret, claims_cls=CodeIDToken)
    claims.validate()
    request.session['token'] = token
    request.session['user'] = claims

    redir_uri = f"http://localhost:5173/" 
    return redirect(redir_uri)


@csrf_exempt
def logout(request):
    response = HttpResponseRedirect(
        'https://jaccount.sjtu.edu.cn/oauth2/logout?' +
        urlencode({
            'client_id': JACCOUNT_CLIENT_ID,
            'post_logout_redirect_uri': request.build_absolute_uri('/logged_out'),
            # 'state': '' # jAccount后台对该参数的处理疑似存在 bug，会在 state 前错误添加 ? 和 &，遂弃用
        })
    )
    response.delete_cookie('sessionid')  # 指示客户端清除 cookie 会话
    return response


@csrf_exempt
def logged_out(request):
    # redir_uri = request.build_absolute_uri('/index')
    redir_uri = "http://localhost:5173/"
    return HttpResponseRedirect(redir_uri)

@csrf_exempt
def jac(request):
    token = request.session['token']
    access_token = token['access_token']
    requests.packages.urllib3.disable_warnings()
    result = requests.get(f'https://api.sjtu.edu.cn/v1/me/profile?access_token={access_token}', verify=False)
    return result.json()