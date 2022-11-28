"""
Database models.
"""
import uuid
import os

from datetime import datetime


from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def user_image_file_path(instance, filename):
    """Generate file path for new user image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'user', filename)

def user_header_image_file_path(instance, filename):
    """Generate file path for new user header image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'header', filename)

def post_image_file_path(instance, filename):
    """Generate file path for new post image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'post', filename)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    # User data
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    birthday =  models.DateField(null = True)
    gender = models.CharField(null = True, max_length = 255)
    username = models.CharField(null = False, max_length = 255)
    phone = models.CharField(null=True, max_length=15, blank=True)
    city = models.CharField(null=True, max_length=255, blank=True)


    profile_picture = models.ImageField(null=True, upload_to=user_image_file_path)
    cover_picture = models.ImageField(null=True, upload_to=user_header_image_file_path)

    # User links
    website_link = models.URLField(null=True, blank=True)
    github_link =  models.URLField(null=True, blank=True)
    twitter_link =  models.URLField(null=True, blank=True)
    instagram_link =  models.URLField(null=True, blank=True)
    facebook_link =  models.URLField(null=True, blank=True)
    

    is_online = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Post(models.Model):
    """Post object in the system"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default="Free"
    )
    description = models.CharField(max_length=1000, null= True, blank=True) 
    post_image = models.ImageField(null=True, upload_to=post_image_file_path, blank=True, )
    publish_date = models.DateTimeField(auto_now_add=True)

    comments = models.ManyToManyField("Comment", null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    """Comment object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    comment = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)