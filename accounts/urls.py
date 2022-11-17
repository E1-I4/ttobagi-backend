from django.urls import path, include
from .views import UserList,UserDetail
from .kakao import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('list',UserViewSet)

urlpatterns = [
    path("list/",UserList.as_view()),
    path("list/<int:pk>/",UserDetail.as_view()),
    path("kakao/login",kakao_login,name="kakao_login"),
    path("kakao/callback/",kakao_callback,name="kakao_callback"),
    path("kakao/login/finish", KakaoLogin.as_view(),name="kakao_login_todjango"),
]