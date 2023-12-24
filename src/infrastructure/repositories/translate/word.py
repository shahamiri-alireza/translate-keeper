from uuid import UUID

from infrastructure.repositories.generic import GenericRepository
from domain.apps.translate.models import Word
from infrastructure.serializers.translate.word import WordModelSerializer


class WordRepository(GenericRepository):
    model = Word
    serializer_class = WordModelSerializer
