import datetime
import uuid
from datetime import timedelta
import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# def check_number(r):
#     return len(r)==13

class RoleChoice(models.TextChoices):
    READER = ('Reader', 'reader')  # read,upload
    ADMIN = ('Admin', 'admin')  # crud
    PUBLISHER = ('Publisher', 'publisher')  # read update


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    role = models.CharField(default=RoleChoice.READER, choices=RoleChoice, max_length=15)
    email = models.EmailField(max_length=254)


def check_date():
    return timezone.now() + datetime.timedelta(minutes=2)




def random_code():
    return str(random.randint(100000, 999999))


class Code(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='code')
    expire_date = models.DateTimeField(default=check_date)
    code =models.CharField(max_length=100, default=random_code)

    def __str__(self):
        return self.code
