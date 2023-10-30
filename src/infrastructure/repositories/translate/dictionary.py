from uuid import UUID

from infrastructure.repositories.generic import GenericRepository
from domain.apps.translate.models import Dictionary
from infrastructure.serializers.translate.dictionary import DictionaryModelSerializer


class DictionaryRepository(GenericRepository):
    model = Dictionary
    serializer_class = DictionaryModelSerializer
