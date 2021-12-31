from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet
from shared.mixins import DynamicPermissionsMixin, DynamicSerializersMixin
from shared.permissions import IsOwner
from .serializers import FullUserSerializer, UpdateUserSerializer, UserSerializer
from .models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class UserViewSet(DynamicSerializersMixin,
                  DynamicPermissionsMixin,
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
    }

    serializer_classes_by_action = {
        'update': UpdateUserSerializer,
        'partial_update': UpdateUserSerializer,
        'get_current_user': FullUserSerializer,
        'get_user_snippets': SnippetSerializer,
    }

    @action(methods=["get"], detail=False, url_path='(?P<username>[^/.]+)', url_name="user")
    def get_user_by_username(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path='me', url_name="me")
    def get_current_user(self, request):

        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path='(?P<username>[^/.]+)/snippets', url_name="snippets")
    def get_user_snippets(self, request, username):

        user_snippets = Snippet.objects.all().filter(user__username=username)

        page = self.paginate_queryset(user_snippets)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(user_snippets, many=True)
        return Response(serializer.data)
