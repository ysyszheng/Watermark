from django.db import models


class User(models.Model):
    user_name = models.CharField('用户名', max_length=30)
    jaccount = models.CharField('Jaccount', max_length=30, unique=True)

    # is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self):
        return '%s' % self.user_name


class Wallpaper(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    username = models.CharField(max_length=64, default='visitor')
    photo = models.ImageField(upload_to='', default="#")
    photo_name = models.CharField(max_length=120, default='visitor.jpg')
    css = models.CharField(max_length=120, default="")

    class Meta:
        db_table = 'Wallpaper'
        verbose_name = 'Wallpaper'
        verbose_name_plural = 'Wallpaper'

    def __str__(self):
        return '%s' % self.username