from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_id = models.BigIntegerField(null=True, unique=True)
    phone_number = models.CharField(null=True, unique=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

