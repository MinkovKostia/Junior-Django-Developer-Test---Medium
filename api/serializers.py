from string import Template
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: tuple = ('first_name', 'last_name', 'username')


class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields: tuple = ('id', 'user', 'phone_number', 'birth_date')
