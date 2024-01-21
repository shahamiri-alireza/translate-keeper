from uuid import UUID

from attrs import define


@define
class TempWordDto:
    id: UUID
    dictionaryId: UUID
    title: str
    description: str
