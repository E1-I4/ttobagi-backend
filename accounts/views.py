
from .models import User
from .serializers import UserSerializer,AnimalSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from animal_dictionary.models import Animal

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True,is_superuser=False).all()
    serializer_class = UserSerializer
    
class UserAnimalList(generics.ListAPIView):
    serializer_class = AnimalSerializer
    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user.animals.all()

@api_view(['POST'])
def add_animal(request,pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        animal = Animal.objects.get(id=request.data['id'])
        if animal:
            user.animals.add(animal)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)