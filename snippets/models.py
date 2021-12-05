from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, default='')
