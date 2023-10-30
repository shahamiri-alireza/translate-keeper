from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from application.permissions.permissions import CurrentUserOrAdmin
from infrastructure.commands.translate.dictionary import DictionaryCommand
from infrastructure.serializers.translate.dictionary import DictionaryModelSerializer
from domain.apps.translate.models import Dictionary
from infrastructure.serializers.translate.language import LanguageModelSerializer

class DictionaryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, CurrentUserOrAdmin)

    def get_serializer_class(self):
        if self.action == "language_list":
            return LanguageModelSerializer
        else:
            return DictionaryModelSerializer

    def get_queryset(self):
        print(self.request.user)
        return Dictionary.objects.filter(user=self.request.user)

    @action(methods=["get"], detail=True)
    def language_list(self, request, pk=None):
        command = DictionaryCommand()
        response = command.get_languages(pk=pk)

        return Response(data={"data": {"items": response}}, status=status.HTTP_200_OK)
