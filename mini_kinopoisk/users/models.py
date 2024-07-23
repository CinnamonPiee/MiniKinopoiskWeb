from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60, null=False, unique=True)
    phone_number = models.CharField(max_length=15, null=False, unique=True)
    telegram_id = models.BigIntegerField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)