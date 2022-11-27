from .models import Animal
from rest_framework import serializers
    
class AnimalSerializer(serializers.ModelSerializer):
    animal_name = serializers.ImageField(use_url=True)
    animal_name_color = serializers.ImageField(use_url=True)
    image = serializers.ImageField(use_url=True)
    trash = serializers.ImageField(use_url=True)
    target = serializers.ImageField(use_url=True)
    sick = serializers.ImageField(use_url=True)
    sil = serializers.ImageField(use_url=True)
    class Meta:
        model = Animal
        fields = ('id','name','animal_name','animal_name_color','trash_name','description','trash_description','image','trash','target','sil','sick','latitude','longtitude')