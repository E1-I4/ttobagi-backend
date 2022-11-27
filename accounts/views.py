
from .models import User
from .serializers import UserSerializer,AnimalSerializer,IDSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from animal_dictionary.models import Animal
from rest_framework.renderers import JSONRenderer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True,is_superuser=False).all()
    serializer_class = UserSerializer
    
class UserAnimalList(generics.ListAPIView):
    serializer_class = AnimalSerializer
    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return user.animals.all()
    
    def list(self,reqeust,*args,**kwargs):
        id_set = self.get_queryset().values('id')
        id_serializer = IDSerializer(id_set,many=True)
        return Response(data=id_serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_animal(request,pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        animal = Animal.objects.get(id=request.data['id'])
        if animal:
            user.animals.add(animal)
            return Response(data={'message':f'animal {animal.name} is added'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)