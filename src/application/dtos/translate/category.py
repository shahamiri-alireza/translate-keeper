from uuid import UUID

from attrs import define
from .dictionary import DictionaryDto
from ..base import BaseDto


@define
class CategoryDto(BaseDto):
    # dictionary: DictionaryDto
    title: str = ""
    color: str = ""
