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

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh_token'])
        data = {'access_token':str(refresh.access_token)}
        return data

class IDSerializer(serializers.Serializer):
    id = serializers.IntegerField()