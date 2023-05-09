from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified_email = models.BooleanField(default=False, null=True)
