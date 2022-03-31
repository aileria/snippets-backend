from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from shared.mixins import DynamicPermissionsMixin, DynamicSerializersMixin, PaginationMixin
from shared.permissions import IsOwner
from .serializers import FullUserSerializer, UpdateUserSerializer, UserSerializer
from .models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter


@extend_schema_view(
    list=extend_schema(description='Get paginated list of users.'),
    update=extend_schema(description='Update user data.'),
    partial_update=extend_schema(description='Partially update user data.'),
    destroy=extend_schema(description='Delete a user.'),
    get_user_snippets=extend_schema(
        description='Get paginated list of the specified user\'s snippets.',
        parameters=[
            OpenApiParameter(
                name='page',
                type=str,
                location=OpenApiParameter.QUERY,
                required=False,
            )]),
    get_current_user_snippets=extend_schema(
        description='Get paginated list of the currently logged user\'s snippets.',
        parameters=[
            OpenApiParameter(
                name='page',
                type=str,
                location=OpenApiParameter.QUERY,
                required=False,
            )])
)
class UserViewSet(DynamicSerializersMixin,
                  DynamicPermissionsMixin,
                  PaginationMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {
        'update': (permissions.IsAdminUser | IsOwner,),
        'partial_update': (permissions.IsAdminUser | IsOwner,),
        'destroy': (permissions.IsAdminUser | IsOwner,),
        'get_current_user': (permissions.IsAuthenticated,),
        'get_current_user_snippets': (permissions.IsAuthenticated,),
    }

    serializer_classes_by_action = {
        'update': UpdateUserSerializer,
        'partial_update': UpdateUserSerializer,
        'get_current_user': FullUserSerializer,
        'get_user_snippets': SnippetSerializer,
        'get_current_user_snippets': SnippetSerializer,
    }

    @action(methods=["get"], detail=False, url_path='(?P<username>[^/.]+)', url_name="user")
    def get_user_by_username(self, request, username):
        """Get user data by username."""

        user = get_object_or_404(User, username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path='me', url_name="me")
    def get_current_user(self, request):
        """Get currently logged user data."""

        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path='(?P<username>[^/.]+)/snippets', url_name="snippets")
    def get_user_snippets(self, request, username):
        """Get snippets created by the specified user."""

        user_snippets = Snippet.objects.all().filter(user__username=username).order_by('-id')
        return self.paginated_response(user_snippets)

    @action(methods=["get"], detail=False, url_path='me/snippets', url_name="my-snippets")
    def get_current_user_snippets(self, request):
        """Get snippets created by currently logged user."""

        user_snippets = Snippet.objects.all().filter(user=request.user).order_by('-id')
        return self.paginated_response(user_snippets)
