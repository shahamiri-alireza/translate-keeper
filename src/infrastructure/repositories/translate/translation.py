from infrastructure.repositories.generic import GenericRepository
from domain.apps.translate.models import Translation
from infrastructure.serializers.translate.translation import TranslationModelSerializer


class TranslationRepository(GenericRepository):
    model = Translation
    serializer_class = TranslationModelSerializer
