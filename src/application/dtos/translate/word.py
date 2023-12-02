from uuid import UUID

from attrs import define

from typing import List

from .category import CategoryDto
from .translation import TranslationDto


@define
class WordDto:
    id: UUID
    dictionaryId: UUID
    title: str
    description: str
    category: CategoryDto
    translations: List[TranslationDto]
