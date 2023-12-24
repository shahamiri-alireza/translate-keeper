from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from domain.apps.translate.models import Category, Dictionary
from infrastructure.serializers.translate.dictionary import (
    DictionaryWithoutLanguageSerializer,
)


class CategoryModelSerializer(ModelSerializer):
    dictionary = DictionaryWithoutLanguageSerializer()

    class Meta:
        model = Category
        exclude = ("created_date", "updated_date")

    def to_internal_value(self, data):
        # Override to include 'id' field in validated data
        return data

    def validate(self, data):
        # Check if dictionary is valid before creating the category
        try:
            dictionary = Dictionary.objects.get(id=data["dictionary"]["id"])
            data["dictionary"] = dictionary
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                f"Dictionary with ID {data['dictionary']['id']} does not exist."
            )

        return data

    def create(self, validated_data):
        # Create a new Category instance
        category = Category.objects.create(
            title=validated_data["title"],
            color=validated_data["color"],
            dictionary=validated_data["dictionary"],
        )
        return category

    def update(self, instance: Category, validated_data):
        # Update the Dictionary instance with the user field set
        instance.title = validated_data["title"]
        instance.color = validated_data["color"]
        instance.save()

        return instance


class CategoryModelWithoutDictionarySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ("dictionary", "created_date", "updated_date")
