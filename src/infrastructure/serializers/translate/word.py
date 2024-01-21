from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from domain.apps.translate.models import Dictionary, Word, Category, Translation
from infrastructure.serializers.translate.category import (
    CategoryModelWithoutDictionarySerializer,
)
from infrastructure.serializers.translate.dictionary import (
    DictionaryWithoutLanguageSerializer,
)
from infrastructure.serializers.translate.translation import TranslationModelSerializer


class WordModelSerializer(ModelSerializer):
    translations = TranslationModelSerializer(
        many=True, read_only=True, source="translation_set"
    )
    dictionary = DictionaryWithoutLanguageSerializer()
    category = CategoryModelWithoutDictionarySerializer(many=True)

    class Meta:
        model = Word
        fields = [
            "id",
            "dictionary",
            "title",
            "description",
            "category",
            "translations",
        ]
        # exclude = ("created_date", "updated_date")

    def to_internal_value(self, data):
        # Override to include 'id' field in validated data
        return data

    def validate(self, data):
        try:
            dictionary = Dictionary.objects.get(id=data["dictionary"]["id"])
            data["dictionary"] = dictionary
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                f"Dictionary with ID {data['dictionary']['id']} does not exist."
            )

        valid_categories = []
        for category in data["category"]:
            try:
                cat = Category.objects.get(id=category["id"])
                valid_categories.append(cat)
            except ObjectDoesNotExist:
                raise serializers.ValidationError(
                    f"Category with ID {data['category']['id']} does not exist."
                )

        data["category"] = valid_categories

        return data

    def create(self, validated_data):
        # translations_data = validated_data.pop("translations", [])

        word = Word.objects.create(
            dictionary=validated_data["dictionary"],
            title=validated_data["title"],
            description=validated_data["description"],
            # category=validated_data["category"],
        )

        word.category.set(validated_data["category"])

        # for translation_data in translations_data:
        #     Translation.objects.create(
        #         word=word,
        #         language_id=translation_data["language"]["id"],
        #         translate=translation_data["translate"],
        #     )

        return word

    def update(self, instance: Word, validated_data):
        # translations_data = validated_data.pop("translations", [])

        instance.title = validated_data["title"]
        instance.description = validated_data["description"]
        instance.category.set(validated_data["category"])
        instance.save()

        Translation.objects.filter(word__id=instance.id).delete()

        # for translation_data in translations_data:
        #     Translation.objects.create(
        #         word=instance,
        #         language_id=translation_data["language"]["id"],
        #         translate=translation_data["translate"],
        #     )

        return instance

    # def setTranslations(self, translations):
    #     for translation in translations:
    #         translation.
