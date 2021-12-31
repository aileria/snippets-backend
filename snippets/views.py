from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from shared.views import BaseModelViewSet
from .serializers import FullSnippetSerializer, SnippetFileSerializer, SnippetSerializer
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

    serializer_class = SnippetSerializer
    serializer_classes_by_action = {
        'create': FullSnippetSerializer,
        'retrieve': FullSnippetSerializer,
    }

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }


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
