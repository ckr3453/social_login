from django.contrib import admin
from .models import Blog
from .models import Pictures
# Register your models here.

admin.site.register(Pictures)
admin.site.register(Blog)