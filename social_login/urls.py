from django.contrib import admin
from django.urls import path, include
from s_login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('accounts/', include('allauth.urls')),
]

# allauth라는 소셜로그인 기능을 제공하는 url은 이미 다른곳에 설치가됨.
# url을 갖다 쓰기만하면됨 (allauth 패키지기능)
