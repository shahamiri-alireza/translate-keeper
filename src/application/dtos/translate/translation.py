from uuid import UUID

from attrs import define

from .language import LanguageDto
from .temp_word import TempWordDto
from ..base import BaseDto


@define
class TranslationDto(BaseDto):
    word: TempWordDto
    translate: str
    language: LanguageDto
