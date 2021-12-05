from .views import SnippetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', SnippetViewSet, basename='snippet')

urlpatterns = router.urls