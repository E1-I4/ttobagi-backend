
from .models import User
from .serializers import UserSerializer,AnimalSerializer
from rest_framework import generics

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True,is_superuser=False).all()
    serializer_class = UserSerializer
    
class UserAnimalList(generics.ListAPIView):
    serializer_class = AnimalSerializer
    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user.animals.all()