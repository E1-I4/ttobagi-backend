from django.shortcuts import render
from .serializers import AnimalSerializer
from .models import Animal
from rest_framework import viewsets
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer