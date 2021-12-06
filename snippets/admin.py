from django.contrib import admin
from .models import Snippet, SnippetFile

admin.site.register(Snippet)
admin.site.register(SnippetFile)