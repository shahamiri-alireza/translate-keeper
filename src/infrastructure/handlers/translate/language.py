from infrastructure.handlers.base import BaseHandler
from infrastructure.repositories.translate.language import LanguageRepository
from infrastructure.serializers.translate.language import LanguageModelSerializer


class LanguageHandler(BaseHandler):
    repository = LanguageRepository
    serializer_class = LanguageModelSerializer
