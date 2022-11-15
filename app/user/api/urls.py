

from django.urls import include, path
from rest_framework import routers

from user.api.views import UserViewSet, AllUsersViewSet
from user import views


router = routers.DefaultRouter()
router.register('users', UserViewSet)
# router.register('all-users', AllUsersViewSet)

app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
]