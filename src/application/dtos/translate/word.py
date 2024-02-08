from attrs import define

from typing import List, Optional

from .category import CategoryDto
from .dictionary import DictionaryDto
from .language import LanguageDto

from ..base import BaseDto


@define
class WordDto(BaseDto):
    dictionary: DictionaryDto = DictionaryDto()
    title: str = ""
    description: str = ""
    category: List[CategoryDto] = []


@define
class TranslationDto(BaseDto):
    language: LanguageDto
    word: WordDto = WordDto()
    translate: str = ""
