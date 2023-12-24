from infrastructure.commands.base import BaseCommand
from application.dtos.translate.word import WordDto
from infrastructure.handlers.translate.word import WordHandler


class WordCommand(BaseCommand):
    handler = WordHandler
    Dto = WordDto
