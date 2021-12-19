from .views import TechnologyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TechnologyViewSet, basename='technology')

urlpatterns = router.urls