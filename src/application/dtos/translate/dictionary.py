from attrs import define

from application.dtos.base import BaseDto
from application.dtos.identity.user import UserDto


@define
class DictionaryDto(BaseDto):
    # user: UserDto
    name: str = ""
