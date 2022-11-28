from django.urls import path
from .views import UserDetail,UserAnimalList, add_animal, delete_animal
from .kakao import kakao_callback,KakaoLogin

urlpatterns = [
    path("<int:pk>/",UserDetail.as_view()),
    path('<int:pk>/animals/',UserAnimalList.as_view()),
    path('<int:pk>/animals/add/',add_animal),
    path('<int:pk>/animals/delete/',delete_animal),
    path("kakao/callback/",kakao_callback,name="kakao_callback"),
    path("kakao/login/finish/", KakaoLogin.as_view(),name="kakao_login_todjango"),
]