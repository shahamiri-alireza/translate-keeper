from uuid import UUID

from attrs import define


@define
class LanguageDto:
    id: UUID = ""
    name: str = ""
    native_name: str = ""
    abbreviation: str = ""
    rtl: bool = False
