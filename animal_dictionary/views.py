from .serializers import AnimalSerializer
from .models import Animal
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    
    return Response(status=status.HTTP_200_OK)