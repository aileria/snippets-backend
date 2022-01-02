from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

from topics.models import Topic

User = get_user_model()


class Snippet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, default='')
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='snippets',
        related_query_name='snippet'
    )
    topics = models.ManyToManyField(
        Topic, related_name='snippets')


class SnippetFile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField(max_length=25000, blank=False)
    snippet = models.ForeignKey(
        Snippet,
        on_delete=CASCADE,
        related_name='files',
        related_query_name='file'
    )
