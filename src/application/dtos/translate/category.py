from uuid import UUID

from attrs import define
from .dictionary import DictionaryDto
from ..base import BaseDto


@define
class CategoryDto(BaseDto):
    title: str = ""
    color: str = ""
