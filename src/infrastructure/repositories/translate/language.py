from infrastructure.repositories.generic import GenericRepository
from domain.apps.translate.models import Language
from infrastructure.serializers.translate.language import LanguageModelSerializer


class LanguageRepository(GenericRepository):
    model = Language
    serializer_class = LanguageModelSerializer
