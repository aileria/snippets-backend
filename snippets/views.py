from rest_framework import viewsets, permissions
from .serializers import FullSnippetSerializer, SnippetFileSerializer, SnippetSerializer
from .models import Snippet, SnippetFile

class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = (permissions.AllowAny,)

    permission_classes_by_action = {
        'create': permission_classes,
        'list': permission_classes,
        'retrieve': permission_classes,
        'update': permission_classes,
        'partial_update': permission_classes,
        'destroy': permission_classes,
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]

class SnippetViewSet(BaseModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "update": (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        "destroy": (permissions.IsAuthenticated,),
    }

    def get_serializer_class(self):
        if self.action in ('create', 'retrieve'):
            return FullSnippetSerializer
        else:
            return SnippetSerializer

class SnippetFileViewSet(BaseModelViewSet):
    queryset = SnippetFile.objects.all()
    serializer_class = SnippetFileSerializer
    
    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "update": (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        "destroy": (permissions.IsAuthenticated,),
    }