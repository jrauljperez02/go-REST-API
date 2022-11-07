"""
URL mapping for the user API
"""
from django.urls import path
from user.api import views

urlpatterns = [
    path('me/', views.ManageUserView.as_view(), name = 'me'),
]