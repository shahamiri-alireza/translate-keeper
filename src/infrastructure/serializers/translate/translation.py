from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from domain.apps.translate.models import Translation, Language, Word
from infrastructure.serializers.translate.language import LanguageModelSerializer


class TranslationModelSerializer(ModelSerializer):
    language = LanguageModelSerializer

    class Meta:
        model = Translation
        fields = ["id", "translate", "language"]

    def to_internal_value(self, data):
        # Override to include 'id' field in validated data
        return data

    def validate(self, data):
        try:
            language = Language.objects.get(id=data["language"]["id"])
            data["language"] = language
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                f"Language with ID {data['language']['id']} does not exist."
            )

        try:
            word = Word.objects.get(id=data["word"]["id"])
            data["word"] = word
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                f"Word with ID {data['word']['id']} does not exist."
            )

        return data

    def create(self, validated_data):
        translation = Translation.objects.create(
            word=validated_data["word"],
            translate=validated_data["translate"],
            language=validated_data["language"],
        )
        return translation

    def update(self, instance: Translation, validated_data):
        instance.translate = validated_data["translate"]
        instance.language = validated_data["language"]
        instance.save()

        return instance
