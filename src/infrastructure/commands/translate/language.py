from infrastructure.commands.base import BaseCommand
from application.dtos.translate.language import LanguageDto
from infrastructure.handlers.translate.language import LanguageHandler


class LanguageCommand(BaseCommand):
    handler = LanguageHandler
    Dto = LanguageDto
