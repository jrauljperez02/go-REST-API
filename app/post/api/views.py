"""
Views for post APIs
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Post
from post.api import serializers

class PostViewSet(viewsets.ModelViewSet):
    """View for manage post APIs"""

    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve posts for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)