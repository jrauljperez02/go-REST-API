"""
URL mapping for the user API
"""
from django.urls import path
from user import views

urlpatterns = [
    path('me/', views.ManageUserView.as_view(), name = 'me'),
]