import requests
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework import status
from .models import User
from backend.settings import environ,BASE_DIR
import os
from django.views.decorators.csrf import csrf_exempt


env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# KAKAO
BASE_URL = "https://api.ttobagi.site/"
KAKAO_CALLBACK_URI_REACT = "https://www.ttobagi.site/kakaoLogin"
KAKAO_CALLBACK_URI = KAKAO_CALLBACK_URI_REACT

@csrf_exempt
def kakao_callback(request):
    client_id = env('KAKAO_REST_API_KEY')
    code = request.GET.get('code')
    
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
    token_response_json = token_request.json()
    error = token_response_json.get('error', None)
    if error is not None:
        raise JSONDecodeError('kakao token error',error,0)
    
    access_token = token_response_json.get('access_token')
    
    profile_request = requests.post("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()

    kakao_account = profile_json.get('kakao_account')
    email = kakao_account.get('email', None)
            
    if email is None:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Signin 
    try:
        user = User.objects.get(email=email)
        social_user = SocialAccount.objects.get(user=user)
        if social_user == None:
            return JsonResponse({'message': 'kakao email is not registered'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 기존 가입된 유저
        data = {'access_token': access_token,'code': code}
        accept = requests.post(BASE_URL + 'api/user/kakao/login/finish/', data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'message': 'kakao login failed'}, status=accept_status)
        accept_json = accept.json()
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 신규 가입
        data = {'access_token': access_token,'code': code}
        accept = requests.post(BASE_URL + 'api/user/kakao/login/finish/', data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'message': 'kakao signup failed'}, status=accept_status)
        accept_json = accept.json()
        
        return JsonResponse(accept_json)
    

    
class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client
