from rest_framework.viewsets import ModelViewSet
from ..serializers import CategorySerializer
from ....models import Category
from rest_framework.permissions import IsAuthenticated

class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user.id)

    def perform_create(self, serializer):
        user_id = self.request.user
        serializer.save(user=user_id)
