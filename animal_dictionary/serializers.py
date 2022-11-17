from .models import Animal
from rest_framework import serializers
    

class AnimalSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    trashes = serializers.ImageField(use_url=True)
    class Meta:
        model = Animal
        fields = ('name','description','image','trashes','latitude','longtitude','owners')