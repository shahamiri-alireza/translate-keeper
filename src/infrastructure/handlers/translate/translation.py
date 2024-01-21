from infrastructure.handlers.base import BaseHandler
from infrastructure.repositories.translate.translation import TranslationRepository
from infrastructure.serializers.translate.translation import TranslationModelSerializer


class TranslationHandler(BaseHandler):
    repository = TranslationRepository
    serializer_class = TranslationModelSerializer
