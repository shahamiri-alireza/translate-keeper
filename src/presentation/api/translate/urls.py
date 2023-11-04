from django.urls import path
from rest_framework.routers import DefaultRouter

from presentation.controllers.translate.dictionary import DictionaryModelViewSet
from presentation.controllers.translate.language import LanguageViewSet

router = DefaultRouter()
router.register("dictionary", DictionaryModelViewSet, basename="/dictionary")

urlpatterns = [
    path("language/list/", LanguageViewSet.as_view({"get": "list"}), name="language")
]

urlpatterns += router.urls