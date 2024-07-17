from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver

class User(AbstractUser):
    matriculation_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, default=make_password('pbkdf2_sha256$720000$6qp1JdnlPDpFYFAS5dC0P9$j1JwIJ/ISv8EIfGHBKUJT9kDamt1ICmPFPLDGY36G08='))

    REQUIRED_FIELDS = ['email', 'matriculation_number', 'full_name']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username if self.username else self.full_name

@receiver(pre_save, sender=User)
def set_unique_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = f'user_{instance.pk or User.objects.count() + 1}'
