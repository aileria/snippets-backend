from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        ordering = ['-id']
