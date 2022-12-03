from rest_framework.viewsets import ModelViewSet
from ..serializers import WordSerializer
from ....models import Word
from rest_framework.permissions import IsAuthenticated

class WordModelViewSet(ModelViewSet):
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Word.objects.filter(user=user.id)

    def perform_create(self, serializer):
        user_id = self.request.user
        serializer.save(user=user_id)
