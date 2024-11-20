from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
  first_name = models.CharField(max_length=50, null=True)
  last_name = models.CharField(max_length=50, null=True)
  bio = models.TextField(max_length=500, null=True, blank=True)
  location = models.CharField(max_length=70, null=True)
  groups = models.ManyToManyField(Group, related_name='snacks2school_user_set', blank=True)
  user_permissions = models.ManyToManyField(Permission, related_name='snacks2school_user_set', blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

  def __str__(self):
    return self.username