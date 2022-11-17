from django.urls import path, include
from .views import RegisterAPIView, AuthAPIView, UserViewSet
from .kakao import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list',UserViewSet)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("auth/", AuthAPIView.as_view()), #post - login, delete - logout, get - user name
    path("auth/refresh/", TokenRefreshView.as_view()), # jwt 토큰 재발급
    path("",include(router.urls)),
    path("kakao/login",kakao_login,name="kakao_login"),
    path("kakao/callback/",kakao_callback,name="kakao_callback"),
    path("kakao/login/finish", KakaoLogin.as_view(),name="kakao_login_todjango"),
]