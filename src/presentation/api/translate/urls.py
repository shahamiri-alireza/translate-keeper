from django.urls import path
from rest_framework.routers import DefaultRouter

from presentation.controllers.translate.dictionary import DictionaryModelViewSet
from presentation.controllers.translate.category import CategoryModelViewSet
from presentation.controllers.translate.language import LanguageViewSet
from presentation.controllers.translate.word import WordModelViewSet

router = DefaultRouter()
router.register("dictionary", DictionaryModelViewSet, basename="/dictionary")
router.register("category", CategoryModelViewSet, basename="category")
router.register("word", WordModelViewSet, basename="word")

urlpatterns = [
    path("language/list/", LanguageViewSet.as_view({"get": "list"}), name="language")
]

urlpatterns += router.urls
