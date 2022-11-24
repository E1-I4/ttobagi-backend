from .models import Animal
from rest_framework import serializers
    
class AnimalSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    trash = serializers.ImageField(use_url=True)
    target = serializers.ImageField(use_url=True)
    sick = serializers.ImageField(use_url=True)
    sil = serializers.ImageField(use_url=True)
    class Meta:
        model = Animal
        fields = ('id','name','trash_name','description','trash_description','image','trash','target','sil','sick','latitude','longtitude','owners')