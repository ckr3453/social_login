from django.contrib import admin
from django.urls import path, include
from s_login import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# allauth라는 소셜로그인 기능을 제공하는 url은 이미 다른곳에 설치가됨.
# url을 갖다 쓰기만하면됨 (allauth 패키지기능)
# 미디어 파일을위해 static 함수를 더해줘야함