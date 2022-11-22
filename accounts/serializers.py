from .models import User
from rest_framework import serializers
from animal_dictionary.serializers import AnimalSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    animals = AnimalSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
    # def update(self, instance, validated_data):
    #     animal_data = validated_data.pop('animal')
    #     instance = super(UserSerializer, self).update(instance, validated_data)
        
    #     animal_qs = Animal.objects.filter(pk=animal_data['name'])
        
    #     if animal_qs.exists():
    #         animal = animal_qs.first()
    #         instance.animals.add(animal)

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh_token'])
        data = {'access_token':str(refresh.access_token)}
        return data