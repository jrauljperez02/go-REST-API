"""
Views for the user API
"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.contrib.auth import get_user_model

from rest_framework import generics, authentication, permissions
from rest_framework import viewsets
from user.api.serializers import UserSerializer

from django_filters import rest_framework as filters
        
class UserFilter(filters.FilterSet):
    class Meta:
        model = get_user_model()
        fields = ['username', 'name']
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    permission_classes = [permissions.IsAuthenticated]



@extend_schema_view(
    list = extend_schema(description = 'Allow obtain a account list'),
    retrieve = extend_schema(description = 'Allos obtain a specific account'),
    create = extend_schema(description = 'Allow create a new account'),
    update = extend_schema(description = 'Allow update an existing account'),
    destroy = extend_schema(description = 'Allows delete a account'),
)
class AllUsersViewSet(viewsets.ModelViewSet):
    """View for manage all Posts APIs"""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    permission_classes = [permissions.IsAuthenticated]
