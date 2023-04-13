from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField(unique=True, default='')
    phone_number = models.CharField(max_length=15, unique=True)
    public_key = models.TextField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'phone_number', 'password', 'public_key']
