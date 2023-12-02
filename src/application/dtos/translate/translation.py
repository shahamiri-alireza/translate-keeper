from uuid import UUID

from attrs import define

from .language import LanguageDto
from .word import WordDto


@define
class TranslationDto:
    id: UUID
    word: WordDto
    translate: str
    language: LanguageDto
