from typing import List
from uuid import UUID

from django.db.models.query import Q

from application.dtos.translate.category import CategoryDto
from application.dtos.translate.language import LanguageDto
from domain.apps.translate.models import Translation
from infrastructure.commands.base import BaseCommand
from application.dtos.translate.word import WordDto, TranslationDto

# from application.dtos.translate.translation import TranslationDto
from infrastructure.handlers.translate.translation import TranslationHandler
from infrastructure.handlers.translate.word import WordHandler
from infrastructure.services.dto import DtoService


class WordCommand(BaseCommand):
    handler = WordHandler
    Dto = WordDto
    translation_dto = TranslationDto
    translation_handler = TranslationHandler

    def cast_target_dto(self, data, dto):
        dto_service = DtoService()
        return dto_service.cast(data, dto)

    def create(self, data, serialize=True):
        handler = self.handler()
        translation_handler = self.translation_handler()

        word_dto = self.cast_target_dto(data, self.Dto)
        word = handler.create(word_dto)

        translations = data["translations"]
        for translation in translations:
            translation["word"] = word

        translations_dto = self.cast_target_dto(
            translations, List[self.translation_dto]
        )

        translation_handler.bulk_create(translations_dto)

        return word["id"]

    def update(self, data, serialize=True):
        handler = self.handler()
        translation_handler = self.translation_handler()

        word_dto = self.cast_target_dto(data, self.Dto)
        word = handler.update(word_dto)

        translation_handler.delete(Q(word__id=word["id"]))

        translations = data["translations"]
        for translation in translations:
            translation["word"] = word

        translations_dto = self.cast_target_dto(
            translations, List[self.translation_dto]
        )

        translation_handler.bulk_create(translations_dto)

        return word["id"]
