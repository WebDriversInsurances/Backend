from rest_framework import serializers
from .models import *


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Driver
        # Поля, которые мы сериализуем (Все поля)
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['login']

class InsuranceSerializer(serializers.ModelSerializer):
    drivers = DriverSerializer(read_only=True, many=True)
    users = UserSerializer(read_only=True)
    moderator = UserSerializer(read_only=True)
    class Meta:
        # Модель, которую мы сериализуем
        model = Insurance
        # Поля, которые мы сериализуем (Все поля)
        fields = '__all__'
