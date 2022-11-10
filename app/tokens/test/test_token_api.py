"""
Tests for JWT APIs
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient

def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


TOKENS_URL = reverse('token:token_obtain_pair')

class AuthViewsTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')

    def test_current_user(self):

        # Create a user is a workaround in order to authentication works
        self.assertEqual(self.user.is_active, 1, 'Active User')

        #TODO Create unit tests to handle JWT APIs