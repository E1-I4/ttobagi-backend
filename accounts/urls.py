from django.urls import path
from .views import UserDetail,UserAnimalList, add_animal
from .kakao import kakao_callback,kakao_login,KakaoLogin

urlpatterns = [
    path("<int:pk>/",UserDetail.as_view()),
    path('<int:pk>/animals/',UserAnimalList.as_view()),
    path('<int:pk>/animals/add/',add_animal),
    path("kakao/dlogin/",kakao_login,name="kakao_login"),
    path("kakao/callback/",kakao_callback,name="kakao_callback"),
    path("kakao/login/finish/", KakaoLogin.as_view(),name="kakao_login_todjango"),
]