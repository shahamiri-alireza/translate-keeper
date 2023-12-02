from uuid import UUID

from attrs import define
from .dictionary import DictionaryDto


@define
class CategoryDto:
    id: UUID
    title: str
    color: str
    dictionary: DictionaryDto
