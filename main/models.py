from django.db import models
from django.contrib.auth.models import User


class ContactForm(models.Model):
    username = models.CharField(verbose_name="Имя", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return "{0} - ({1})".format(self.username, self.email)
