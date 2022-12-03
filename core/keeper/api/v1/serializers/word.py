from rest_framework import serializers
from ....models import Word, Category
from .category import CategorySerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'translate', 'description', 'categories']


    def to_representation(self, instance):
        rep = super().to_representation(instance)

        categories = []
        try:
            for category_id in rep['categories']:
                category = Category.objects.get(id=category_id, user=instance.user)
                categories.append(CategorySerializer(category).data)

            rep['categories'] = categories

        except ObjectDoesNotExist:
            raise ValidationError({'detail':'one or more categories not found'}, code=400)


        return rep