from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from application.permissions.permissions import CurrentUserOrAdmin
from domain.apps.translate.models import Word
from infrastructure.commands.translate.word import WordCommand
from infrastructure.serializers.translate.word import WordModelSerializer


# class WordModelViewSet(ModelViewSet):
#     permission_classes = (IsAuthenticated, CurrentUserOrAdmin)
#     serializer_class = WordModelSerializer
#
#     def get_queryset(self):
#         return Word.objects.filter(dictionary__user=self.request.user)


class WordModelViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated, CurrentUserOrAdmin)
    serializer_class = WordModelSerializer

    def create(self, request):
        command = WordCommand()
        response = command.create(request.data, True)

        return Response(data={"data": {"id": response}}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        command = WordCommand()
        response = command.retrieve(pk)

        return Response(data={"data": response}, status=status.HTTP_200_OK)

    def list(self, request):
        command = WordCommand()
        response = command.list()

        return Response(data={"data": {"items": response}}, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        command = WordCommand()
        response = command.destroy(pk)

        return Response(data={"data": response}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        command = WordCommand()
        response = command.update(request.data)

        return Response(data={"data": response}, status=status.HTTP_200_OK)
