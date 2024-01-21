from uuid import UUID

from attrs import define

from typing import List

from .category import CategoryDto
from .dictionary import DictionaryDto
from .language import LanguageDto

from ..base import BaseDto


@define
class WordDto(BaseDto):
    dictionary: DictionaryDto
    title: str
    description: str
    category: List[CategoryDto]


@define
class TranslationDto:
    word: WordDto
    translate: str
    language: LanguageDto


@define
class WordWithTranslationDto(WordDto):
    translations: List[TranslationDto]
