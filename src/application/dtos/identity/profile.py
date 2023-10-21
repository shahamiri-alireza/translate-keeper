from attrs import define

from application.dtos.base import BaseDto
from application.dtos.identity.user import UserDto

@define
class ProfileDto(BaseDto):
    user: UserDto
    first_name: str
    last_name: str