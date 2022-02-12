from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions, filters, mixins
from rest_framework.viewsets import GenericViewSet
from shared.views import BaseModelViewSet
from .serializers import SnippetWriteSerializer, SnippetFileSerializer, BaseSnippetSerializer, SnippetSerializer
from .models import Snippet, SnippetFile


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippets.'),
    retrieve=extend_schema(description='Get snippet.'),
    create=extend_schema(description='Create snippet.'),
    update=extend_schema(description='Update snippet.'),
    partial_update=extend_schema(description='Partially update snippet.'),
    destroy=extend_schema(description='Delete snippet.'),
)
class SnippetViewSet(BaseModelViewSet):
    queryset = Snippet.objects.all()
    search_fields = ['description', 'file__name', 'file__content', 'topics__name']
    filter_backends = (filters.SearchFilter,)

    serializer_class = SnippetSerializer
    serializer_classes_by_action = {
        'create': SnippetWriteSerializer,
        'update': SnippetWriteSerializer,
        'partial_update': SnippetWriteSerializer,
        'retrieve': SnippetSerializer,
    }

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippets previews.'),
    retrieve=extend_schema(description='Get snippet preview.'),
)
class SnippetPreviewViewSet(mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Snippet.objects.all()
    search_fields = ['description', 'file__name', 'file__content', 'topics__name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BaseSnippetSerializer


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippet files.'),
    retrieve=extend_schema(description='Get snippet file.'),
    create=extend_schema(description='Create snippet file.'),
    update=extend_schema(description='Update snippet file.'),
    partial_update=extend_schema(description='Partially update snippet file.'),
    destroy=extend_schema(description='Delete snippet file.'),
)
class SnippetFileViewSet(BaseModelViewSet):
    queryset = SnippetFile.objects.all()
    serializer_class = SnippetFileSerializer

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }
