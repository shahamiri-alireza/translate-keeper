from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from application.permissions.permissions import CurrentUserOrAdmin
from domain.apps.translate.models import Word
from infrastructure.serializers.translate.word import WordModelSerializer


class WordModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, CurrentUserOrAdmin)
    serializer_class = WordModelSerializer

    def get_queryset(self):
        return Word.objects.filter(dictionary__user=self.request.user)
