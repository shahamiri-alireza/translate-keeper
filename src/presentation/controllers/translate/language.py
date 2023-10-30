from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from application.permissions.permissions import IsAuthenticated
from infrastructure.commands.translate.language import LanguageCommand
from infrastructure.serializers.translate.language import LanguageModelSerializer


class LanguageViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LanguageModelSerializer

    def list(self, request, *args, **kwargs):
        command = LanguageCommand()
        response = command.list(request.user.pk)

        return Response(data={"data": {"items": response}}, status=status.HTTP_200_OK)
