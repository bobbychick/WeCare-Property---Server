from rest_framework import serializers
from .models import CustomUserModel, CustomCompanyModel
from django.db import models
from django.core.exceptions import ValidationError


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["userId", "username", "email", "company", "password"]

    def create(self, validated_data):
        user = CustomUserModel.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
            # validated_data["role"],
        )
        return user
