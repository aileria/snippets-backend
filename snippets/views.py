from rest_framework import viewsets
from .serializers import SnippetSerializer
from .models import Snippet

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer