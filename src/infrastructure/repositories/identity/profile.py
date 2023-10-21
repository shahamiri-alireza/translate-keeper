from time import timezone
from uuid import UUID

from django.db.models import Q, QuerySet

from infrastructure.repositories.generic import GenericRepository
from domain.apps.identity.models import Profile
from infrastructure.serializers.identity.serializers import ProfileModelSerializer


class ProfileRepository(GenericRepository):
    model = Profile
    serializer_class = ProfileModelSerializer
    queryset = Profile.objects.filter(Q(user__is_hidden=False))

    def get_by_user_id(self, user_id: UUID) -> QuerySet:
        return self.get(Q(user__id=user_id))