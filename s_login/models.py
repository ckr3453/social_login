from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    test = models.TextField()

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    # 썸네일을 지정해주기 위해 이미지스펙필드를 사용해서 어떤 이미지소스를 썸네일로 삼을것인지(source), processors는 크기조절(가로,세로)
    # 이미지스펙필드를 사용해서 확장자와 인자 방식도 지정가능함
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120,100)], options={'quality':60})