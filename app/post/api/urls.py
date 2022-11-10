"""
URL mapping for the post app.
"""
from django.urls import (path,include)
from rest_framework.routers import DefaultRouter
from post.api import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
]