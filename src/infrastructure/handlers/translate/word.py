from infrastructure.handlers.base import BaseHandler
from infrastructure.repositories.translate.word import WordRepository
from infrastructure.serializers.translate.word import WordModelSerializer


class WordHandler(BaseHandler):
    repository = WordRepository
    serializer_class = WordModelSerializer
