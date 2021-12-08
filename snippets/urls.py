from .views import SnippetFileViewSet, SnippetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', SnippetViewSet, basename='snippet')
router.register('files', SnippetFileViewSet, basename='file')

urlpatterns = router.urls