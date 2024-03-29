from datetime import datetime
from uuid import UUID

from attrs import define


@define(kw_only=True)
class BaseDto:
    id: str = ""
    created_date: datetime = ""
    updated_date: datetime = ""
