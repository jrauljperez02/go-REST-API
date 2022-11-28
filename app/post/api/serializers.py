"""
Serializers for post APIs
"""
from rest_framework import serializers
from core.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments"""

    class Meta:
        model = Comment
        fields = ["id", "user","comment",]
        read_only_fields = ["id"]

class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""

    # comments = CommentSerializer(many = True, required = False)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'description',
            'post_image',
            'publish_date',
        ]
        read_only_fields = ['id']
    
    # def _get_or_create_comments(self, comments, post):
    #     """Handle getting or creating comments as needed"""
    #     auth_user = self.context["request"].user
    #     for comment in comments:
    #         comment_obj, created = Comment.objects.get_or_create(
    #             user = auth_user,
    #             **comment
    #         )
    #         post.comments.add(comment_obj)

        