"""
Views for the user API
"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.contrib.auth import get_user_model

from rest_framework import generics, authentication, permissions
from rest_framework import viewsets
from user.api.serializers import UserSerializer

from django_filters import rest_framework as filters

class ManageUserView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user. """
        return self.request.user
        
class UserFilter(filters.FilterSet):
    class Meta:
        model = get_user_model()
        fields = {
            'name' : ['icontains'],
        }
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    #permission_classes = [permissions.IsAuthenticated]