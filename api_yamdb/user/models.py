from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE = (
        "admin",
        "moderator",
        "user",
    )
    role = models.CharField(max_length=150, choices=ROLE, default="user")
    username = models.CharField(max_length=150, unique=True)
    bio = models.TextField('bio', blank=True)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = 'users'
