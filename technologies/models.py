from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=30, blank=False)
    snippets = models.ManyToManyField('snippets.Snippet', related_name='technologies')