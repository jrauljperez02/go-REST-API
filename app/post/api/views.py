"""
Views for post APIs
"""
from rest_framework import generics, authentication, permissions
from rest_framework import viewsets

from django_filters import rest_framework as filters
from post.api.serializers import PostSerializer
from core.models import Post

from drf_spectacular.utils import extend_schema, extend_schema_view




class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['user']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class =  PostFilter

    def get_queryset(self):
        """Retrieve posts for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    permission_classes = [permissions.IsAuthenticated]


@extend_schema_view(
    list = extend_schema(description = 'Allow obtain a account list'),
    retrieve = extend_schema(description = 'Allos obtain a specific account'),
    create = extend_schema(description = 'Allow create a new account'),
    update = extend_schema(description = 'Allow update an existing account'),
    destroy = extend_schema(description = 'Allows delete a account'),
)
class AllPostViewSet(viewsets.ModelViewSet):
    """View for manage all Posts APIs"""
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-id')

    permission_classes = [permissions.IsAuthenticated]
