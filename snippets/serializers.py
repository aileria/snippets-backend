from rest_framework import serializers
from shared.serializers import RecursiveField
from topics.models import Topic
from topics.serializers import TopicSerializer
from users.serializers import UserSerializer
from .models import Snippet, File, Comment


# FILE

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id',
                  'name',
                  'content')


# COMMENT

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    replies = RecursiveField(many=True)

    class Meta:
        model = Comment
        fields = ('id',
                  'user',
                  'created_date',
                  'content',
                  'replies')


class CommentWriteSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ('parent', 'content')


# SNIPPET

class BaseSnippetSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'description',
                  'topics')


class SnippetSerializer(BaseSnippetSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = Snippet
        fields = BaseSnippetSerializer.Meta.fields + ('files',)


class SnippetWriteSerializer(BaseSnippetSerializer):
    topic_ids = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), many=True, write_only=True)

    class Meta:
        model = Snippet
        fields = BaseSnippetSerializer.Meta.fields + ('topic_ids',)

    def to_representation(self, instance):
        representation = super(SnippetWriteSerializer,
                               self).to_representation(instance)
        representation['topics'] = TopicSerializer(
            instance.topics.all(), many=True).data
        return representation

    def update(self, instance, validated_data):
        topics = validated_data.pop('topic_ids')

        for field in validated_data:
            setattr(instance, field, validated_data.get(
                field, getattr(instance, field)))
        instance.save()
        instance.topics.set(topics)
        return instance


class SnippetCreateSerializer(SnippetWriteSerializer, SnippetSerializer):
    class Meta:
        model = Snippet
        fields = BaseSnippetSerializer.Meta.fields + ('files', 'topic_ids',)

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        topics = validated_data.pop('topic_ids')
        current_user = self.context.get('request').user

        instance = Snippet.objects.create(
            user=current_user,
            **validated_data)

        files = [File(snippet=instance, **file) for file in files_data]
        File.objects.bulk_create(files)

        instance.topics.set(topics)

        return instance
