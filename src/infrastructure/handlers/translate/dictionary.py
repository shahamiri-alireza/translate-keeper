from uuid import UUID

from django.db.models import QuerySet

from infrastructure.handlers.base import BaseHandler
from infrastructure.repositories.translate.dictionary import DictionaryRepository
from infrastructure.serializers.translate.dictionary import DictionaryModelSerializer
from infrastructure.serializers.translate.language import LanguageModelSerializer


class DictionaryHandler(BaseHandler):
    repository = DictionaryRepository
    serializer_class = DictionaryModelSerializer
    language_serializer_class = LanguageModelSerializer

    def get_languages(self, pk: UUID, serialize=True) -> QuerySet:
        dictionary = self.get_by_pk(pk=pk)
        languages = dictionary.get("language")
        return (
            self.language_serializer_class(languages, many=True).data
            if serialize
            else languages
        )
