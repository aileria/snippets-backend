from rest_framework import serializers
from .models import Snippet, SnippetFile

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description')

class SnippetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetFile
        fields = ('id',
                  'name',
                  'content')

class FullSnippetSerializer(serializers.ModelSerializer):
    files = SnippetFileSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description',
                  'files')

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        
        instance = Snippet.objects.create(**validated_data)
        
        files = [SnippetFile(snippet=instance, **file) for file in files_data]
        SnippetFile.objects.bulk_create(files)
        
        return instance

    def update(self, instance, validated_data):
        files_data = validated_data.pop('files')
        
        for field in validated_data:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()

        files = [SnippetFile(snippet=instance, **file) for file in files_data]
        SnippetFile.objects.bulk_create(files)

        return instance