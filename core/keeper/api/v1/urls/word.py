from ..views.word import WordModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', WordModelViewSet, basename="word")
urlpatterns = router.urls