from rest_framework import serializers
from SnippetAPI.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('SnippetId',
                  'SnippetName',
                  'SnippetDescription')