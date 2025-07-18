from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, null=False)
    is_moderator = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
