from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import permissions, filters, mixins
from rest_framework.viewsets import GenericViewSet
from shared.filter_backends import TopicsFilterBackend
from shared.mixins import DynamicSerializersMixin, DynamicPermissionsMixin
from shared.views import BaseModelViewSet
from .serializers import SnippetWriteSerializer, FileSerializer, BaseSnippetSerializer, SnippetSerializer, \
    CommentSerializer, CommentWriteSerializer, SnippetCreateSerializer
from .models import Snippet, File, Comment


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippets.', parameters=[
        OpenApiParameter(
            name='topics',
            type={'type': 'array', 'items': {'type': 'number'}},
            location=OpenApiParameter.QUERY,
            required=False,
            explode=False
        )
    ]),
    retrieve=extend_schema(description='Get snippet.'),
    create=extend_schema(description='Create snippet.'),
    update=extend_schema(description='Update snippet.'),
    partial_update=extend_schema(description='Partially update snippet.'),
    destroy=extend_schema(description='Delete snippet.'),
)
class SnippetViewSet(BaseModelViewSet):
    queryset = Snippet.objects.all()
    search_fields = ['name', 'description', 'file__name', 'file__content']
    filter_backends = (TopicsFilterBackend, filters.SearchFilter)

    serializer_class = SnippetSerializer
    serializer_classes_by_action = {
        'create': SnippetCreateSerializer,
        'update': SnippetWriteSerializer,
        'partial_update': SnippetWriteSerializer,
    }

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippets previews.', parameters=[
        OpenApiParameter(
            name='topics',
            type={'type': 'array', 'items': {'type': 'number'}},
            location=OpenApiParameter.QUERY,
            required=False,
            explode=False
        )
    ]),
    retrieve=extend_schema(description='Get snippet preview.'),
)
class SnippetPreviewViewSet(mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Snippet.objects.all()
    search_fields = ['name', 'description', 'file__name', 'file__content']
    filter_backends = (TopicsFilterBackend, filters.SearchFilter)
    serializer_class = BaseSnippetSerializer


@extend_schema_view(
    list=extend_schema(description='Get paginated list of snippet\'s files.'),
    retrieve=extend_schema(description='Get snippet\'s file.'),
    create=extend_schema(description='Create snippet\'s file.'),
    update=extend_schema(description='Update snippet\'s file.'),
    partial_update=extend_schema(description='Partially update snippet\'s file.'),
    destroy=extend_schema(description='Delete snippet\'s file.'),
)
class FileViewSet(BaseModelViewSet):
    serializer_class = FileSerializer

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }

    def get_queryset(self):
        snippet_id = self.kwargs['snippet_id']
        get_object_or_404(Snippet, id=snippet_id)
        return File.objects.filter(snippet__id=snippet_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['snippet_id'] = self.kwargs['snippet_id']
        context['user'] = self.request.user
        return context

    def perform_create(self, serializer):
        snippet_id = self.kwargs['snippet_id']
        get_object_or_404(Snippet, id=snippet_id)
        serializer.save(snippet_id=snippet_id)

    def perform_update(self, serializer):
        snippet_id = self.kwargs['snippet_id']
        get_object_or_404(Snippet, id=snippet_id)
        serializer.save()


@extend_schema_view(
    list=extend_schema(description='Get list of snippet\'s comments.'),
    create=extend_schema(description='Create snippet\'s comment.'),
    destroy=extend_schema(description='Delete snippet\'s comment.'),
)
class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     DynamicSerializersMixin,
                     DynamicPermissionsMixin,
                     GenericViewSet):
    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAdminUser,),
    }

    serializer_class = CommentSerializer
    serializer_classes_by_action = {
        'list': CommentSerializer,
        'create': CommentWriteSerializer,
    }

    def get_queryset(self):
        snippet_id = self.kwargs['snippet_id']
        get_object_or_404(Snippet, id=snippet_id)
        return Comment.objects.filter(snippet__id=snippet_id, active=True)

    def perform_create(self, serializer):
        user = self.request.user
        snippet_id = self.kwargs['snippet_id']
        serializer.save(user=user, snippet_id=snippet_id)
