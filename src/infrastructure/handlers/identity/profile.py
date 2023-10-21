from uuid import UUID

from django.db.models import QuerySet

from infrastructure.handlers.base import BaseHandler
from infrastructure.repositories.identity.profile import ProfileRepository
from infrastructure.serializers.identity.serializers import ProfileModelSerializer


class ProfileHandler(BaseHandler):
    repository = ProfileRepository
    serializer_class = ProfileModelSerializer

    def get_by_user_id(self, user_id: UUID, serialize=True) -> QuerySet:
        repository = self.repository()
        result = repository.get_by_user_id(user_id=user_id)
        return self.serializer_class(result).data if serialize else result
