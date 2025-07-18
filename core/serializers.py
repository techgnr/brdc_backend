from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import User

from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def validate_password(self, value: str) -> str:
        return make_password(value)


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_moderator",
            "is_staff",
        ]
