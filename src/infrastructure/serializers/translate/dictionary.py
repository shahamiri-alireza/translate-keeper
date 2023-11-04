from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from domain.apps.translate.models import Dictionary, Language
from infrastructure.serializers.translate.language import LanguageModelSerializer


class DictionaryModelSerializer(ModelSerializer):
    language = LanguageModelSerializer(many=True)

    class Meta:
        model = Dictionary
        fields = ["id", "name", "language"]

    def to_internal_value(self, data):
        # Override to include 'id' field in validated data
        return data

    def validate(self, data):
        # Extract the 'language' data from the validated data
        language_data = data.get("language", [])

        # Check if all languages are valid before creating the dictionary
        valid_languages = []
        for lang_data in language_data:
            try:
                language = Language.objects.get(id=lang_data["id"])
                valid_languages.append(language)
            except ObjectDoesNotExist:
                raise serializers.ValidationError(
                    f"Language with ID {lang_data['id']} does not exist."
                )

        data[
            "language"
        ] = valid_languages  # Set the 'language' field with valid languages

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user if request else None

        # Create a new Dictionary instance
        dictionary = Dictionary.objects.create(name=validated_data["name"], user=user)

        # Add associated valid languages to the dictionary
        dictionary.language.set(validated_data["language"])

        return dictionary

    def update(self, instance, validated_data):
        # Update the Dictionary instance with the user field set
        instance.name = validated_data["name"]
        instance.save()

        # Remove existing language associations and add the new ones
        instance.language.clear()
        instance.language.add(*validated_data["language"])

        return instance


class DictionaryWithoutLanguageSerializer(ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ("id", "name")
