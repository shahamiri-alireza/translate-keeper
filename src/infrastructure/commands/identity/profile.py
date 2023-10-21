from application.dtos.identity.profile import ProfileDto
from infrastructure.commands.base import BaseCommand
from infrastructure.handlers.identity.profile import ProfileHandler

class ProfileCommand(BaseCommand):
    handler = ProfileHandler
    Dto = ProfileDto

    def retrieve(self, user_id=None, serialize=True):
        handler: ProfileHandler = self.handler()
        return handler.get_by_user_id(user_id=user_id)