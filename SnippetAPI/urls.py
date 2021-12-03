from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from SnippetAPI import views

urlpatterns = [
    url(r'^snippets/$', views.snippetApi),
    url(r'^snippets/([0-9]+)', views.snippetApi),
]
