from django.contrib import admin

# Register your models here.
from .models import User, Image


class UserManager(admin.ModelAdmin):
    list_display = ['user_name', 'jaccount']
    list_display_links = ['user_name']
    search_fields = ['user_name']


admin.site.register(User, UserManager)


class ImageManager(admin.ModelAdmin):
    list_display = ['id', 'user','username', 'text', 'file_time', 'type', 'photo_input', 'photo_output']
    list_display_links = ['username']
    search_fields = ['username']


admin.site.register(Image, ImageManager)