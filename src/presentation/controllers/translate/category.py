from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from application.permissions.permissions import CurrentUserOrAdmin
from infrastructure.serializers.translate.category import CategoryModelSerializer
from domain.apps.translate.models import Category


class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, CurrentUserOrAdmin)
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        return Category.objects.filter(dictionary__user=self.request.user)

    @extend_schema(
        description="Get categories of given dictionary",
        responses=CategoryModelSerializer(many=True),
    )
    @action(
        methods=["get"],
        detail=False,
        url_path="by_dictionary/(?P<dictionary_id>[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?)",
    )
    def by_dictionary(self, request, dictionary_id=None):
        if not dictionary_id:
            return Response(
                {"error": "parameter dictionary_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        queryset = self.filter_queryset(
            self.get_queryset().filter(dictionary__id=dictionary_id)
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
