from django.db import models
from django.db.models.deletion import CASCADE

class Snippet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, default='')

class SnippetFile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=25000, blank=False)
    snippet = models.ForeignKey(
        Snippet,
        on_delete=CASCADE,
        related_name='files',
        related_query_name='file'
    )
