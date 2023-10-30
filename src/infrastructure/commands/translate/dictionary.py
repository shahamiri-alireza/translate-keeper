from infrastructure.commands.base import BaseCommand
from application.dtos.translate.dictionary import DictionaryDto
from infrastructure.handlers.translate.dictionary import DictionaryHandler


class DictionaryCommand(BaseCommand):
    handler = DictionaryHandler
    Dto = DictionaryDto

    def get_languages(self, pk=None, serialize=True):
        handler: DictionaryHandler = self.handler()
        return handler.get_languages(pk=pk, serialize=serialize)
