from rest_framework.serializers import ModelSerializer

from domain.apps.translate.models import Language


class LanguageModelSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
