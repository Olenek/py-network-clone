from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    info = models.CharField(verbose_name="информация о юзере", max_length=255)
