from ..views.category import CategoryModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CategoryModelViewSet, basename="category")
urlpatterns = router.urls