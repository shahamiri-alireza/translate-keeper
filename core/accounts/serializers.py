from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get("first_name")
        user.last_name = self.validated_data.get("last_name")
        user.save(update_fields=["first_name", "last_name"])
