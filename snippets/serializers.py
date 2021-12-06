from rest_framework import serializers
from .models import Snippet, SnippetFile

class SnippetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetFile
        fields = ('id',
                  'name',
                  'content')

class SnippetSerializer(serializers.ModelSerializer):
    files = SnippetFileSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description',
                  'files')