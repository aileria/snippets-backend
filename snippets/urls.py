from .views import SnippetFileViewSet, SnippetViewSet, SnippetPreviewViewSet, SnippetCommentViewSet
from rest_framework.routers import DefaultRouter

app_name = 'snippets'

router = DefaultRouter()
router.register('previews', SnippetPreviewViewSet, basename='preview')
router.register('files', SnippetFileViewSet, basename='file')
router.register('', SnippetViewSet, basename='snippet')
router.register(r'(?P<snippet_id>\d+)/comments', SnippetCommentViewSet, basename='snippet-comments')

urlpatterns = router.urls
