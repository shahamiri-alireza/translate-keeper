from rest_framework import serializers
from accounts.models import User, Profile


class RegisterSerializer(serializers.Serializer):
    """Registration serializer with password checkup"""
    
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )
    password1 = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        fields = ["email", "first_name", "last_name", "password", "password1"]

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        profile_fields = { 'first_name': validated_data.pop("first_name"), 'last_name': validated_data.pop("last_name") }
        user = User.objects.create_user(email=validated_data["email"], password=validated_data["password"])
        Profile.objects.create(user=user, **profile_fields)
        return user
        


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to manage extra user info"""

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
        ]