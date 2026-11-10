from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=150)
    password = serializers.CharField(write_only=True)

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=150)
    password = serializers.CharField(write_only=True)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Username already exists!")

class UserConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=6, max_length=6)