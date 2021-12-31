from rest_framework import permissions
from shared.views import BaseModelViewSet
from .serializers import FullSnippetSerializer, SnippetFileSerializer, SnippetSerializer
from .models import Snippet, SnippetFile


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


class SnippetFileViewSet(BaseModelViewSet):

    queryset = SnippetFile.objects.all()
    serializer_class = SnippetFileSerializer

    permission_classes_by_action = {
        'create': (permissions.IsAuthenticated,),
        'update': (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        'destroy': (permissions.IsAuthenticated,),
    }
