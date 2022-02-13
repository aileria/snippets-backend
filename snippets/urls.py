from .views import SnippetFileViewSet, SnippetViewSet, SnippetPreviewViewSet
from rest_framework.routers import DefaultRouter

app_name = 'snippets'

router = DefaultRouter()
router.register('previews', SnippetPreviewViewSet, basename='preview')
router.register('files', SnippetFileViewSet, basename='file')
router.register('', SnippetViewSet, basename='snippet')

urlpatterns = router.urls