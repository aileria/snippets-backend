from django.contrib import admin
from .models import Snippet, SnippetFile, Comment

admin.site.register(Snippet)
admin.site.register(SnippetFile)
admin.site.register(Comment)
