from django.db import models
from PIL import Image as ImageProcess
from .process.stegan import encodeDataInImage, decodeImage
from .process.watermark import addWatermark

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


class Image(models.Model):
    user = models.ForeignKey(User, to_field='jaccount', on_delete=models.CASCADE, default='000')
    username = models.CharField(max_length=64, default='visitor')

    type = models.CharField(max_length=64,default='none')

    text = models.CharField(max_length=64, default='')
    file_time = models.CharField(max_length=120, default='visitor.jpg')
    photo_input = models.ImageField(upload_to='', default="#", verbose_name="Image")
    photo_output = models.CharField(max_length=120, default='visitor_.jpg')

    class Meta:
        db_table = 'Image'
        verbose_name = 'Image'
        verbose_name_plural = 'Image'

    def __str__(self):
        return '%s' % self.username
    
    def stegan(self, text):
        filename = self.photo_input.path
        img = ImageProcess.open(filename)
        file = encodeDataInImage(img, text)
        file.save(f"media/stegan_{self.photo_input.__dict__['name']}")
        self.photo_output = f"stegan_{self.photo_input.__dict__['name']}"
        self.type = "stegan"
        self.save()

    def unstegan(self):
        filename = self.photo_input.path
        img = ImageProcess.open(filename)
        text = decodeImage(img)
        self.text = text
        self.type = "unstegan"
        self.save()

    def watermark(self, text):
        filename = self.photo_input.path
        img = ImageProcess.open(filename)
        file = addWatermark(img, text)
        file.save(f"media/watermark_{self.photo_input.__dict__['name']}")
        self.photo_output = f"watermark_{self.photo_input.__dict__['name']}"
        self.type = "watermark"
        self.save()