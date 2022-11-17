from .models import User
from rest_framework import serializers
from animal_dictionary.serializers import AnimalSerializer


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