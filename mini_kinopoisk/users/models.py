from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_id = models.BigIntegerField(null=True, unique=True, blank=True)
    phone_number = models.CharField(null=True, unique=True, blank=True)
    image = models.ImageField(upload_to="user_images/", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

