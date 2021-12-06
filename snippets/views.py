from rest_framework import viewsets
from .serializers import FullSnippetSerializer, SnippetFileSerializer, SnippetSerializer
from .models import Snippet, SnippetFile

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get_serializer_class(self):
        if self.action in ('create', 'retrieve'):
            return FullSnippetSerializer
        else:
            return SnippetSerializer

class SnippetFileViewSet(viewsets.ModelViewSet):
    queryset = SnippetFile.objects.all()
    serializer_class = SnippetFileSerializer