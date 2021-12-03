from django.db import models

# Create your models here.
class Snippet(models.Model):
    SnippetId = models.AutoField(primary_key=True)
    SnippetName = models.CharField(max_length=255)
    SnippetDescription = models.CharField(max_length=25000)