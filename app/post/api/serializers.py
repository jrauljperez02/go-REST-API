"""
Serializers for post APIs
"""
from rest_framework import serializers
from core.models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""

    class Meta:
        model = Post
        fields = [
            'id',
            'description',
            'post_image',
            'publish_date',
        ]
        read_only_fields = ['id']
        