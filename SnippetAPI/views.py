from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from SnippetAPI.models import Snippet
from SnippetAPI.serializers import SnippetSerializer


@csrf_exempt
def snippetApi(request, id=0):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        snippets_serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(snippets_serializer.data, safe=False)
    elif request.method == 'POST':
        snippet_data = JSONParser().parse(request)
        snippets_serializer = SnippetSerializer(data=snippet_data)
        if snippets_serializer.is_valid():
            snippets_serializer.save()
            return JsonResponse("Snippet generated!", safe=False)
        return JsonResponse("Snippet generation failed!", safe=False)
    elif request.method == 'PUT':
        snippet_data = JSONParser().parse(request)
        snippet = Snippet.objects.get(SnippetId=snippet_data['SnippetId'])
        snippets_serializer = SnippetSerializer(snippet, data=snippet_data)
        if snippets_serializer.is_valid():
            snippets_serializer.save()
            return JsonResponse("Snippet updated!", safe=False)
        return JsonResponse("Snippet update failed!", safe=False)
    elif request.method == 'DELETE':
        snippet = Snippet.objects.get(SnippetId=id)
        snippet.delete()
        return JsonResponse("Snippet deleted!", safe=False)
