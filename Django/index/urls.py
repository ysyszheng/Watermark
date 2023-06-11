from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views, axios

urlpatterns = [
    path('', views.index_view, name='index'), 
    path('stegan/', axios.uploadImage_stegan, name="stegan"),
    path('unstegan/', axios.uploadImage_unstegan, name="unstegan"),
    path('watermark/', axios.uploadImage_watermark, name="watermark"),
]