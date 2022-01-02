from rest_framework import serializers
from shared.transactions import bulk_save
from topics.models import Topic

from topics.serializers import TopicSerializer
from .models import Snippet, SnippetFile


class SnippetSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description',
                  'topics')


class SnippetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetFile
        fields = ('id',
                  'name',
                  'content')


class FullSnippetSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)
    files = SnippetFileSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description',
                  'topics',
                  'files')

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        topics_data = validated_data.pop('topics')
        current_user = self.context.get('request').user

        instance = Snippet.objects.create(
            user=current_user,
            **validated_data)

        files = [SnippetFile(snippet=instance, **file) for file in files_data]
        SnippetFile.objects.bulk_create(files)

        topics = [Topic(**topic) for topic in topics_data]
        bulk_save(topics)
        instance.topics.set(topics)

        return instance

    def update(self, instance, validated_data):
        files_data = validated_data.pop('files')
        topics_data = validated_data.pop('topics')

        for field in validated_data:
            setattr(instance, field, validated_data.get(
                field, getattr(instance, field)))
        instance.save()

        files = [SnippetFile(snippet=instance, **file) for file in files_data]
        SnippetFile.objects.bulk_create(files)

        topics = [Topic(**topic) for topic in topics_data]
        bulk_save(topics)
        instance.topics.set(topics)

        return instance
