from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db.models import Avg

# Create your models here.


class systemAccountsManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **otros):

        otros.setdefault('is_staff', True)
        otros.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **otros)

    def create_user(self, email, first_name, last_name, password, **otros):
        if not email:
            raise ValueError('You must provide an email.')
        if not first_name:
            raise ValueError('You must provide an first_name.')
        if not last_name:
            raise ValueError('You must provide an last_name.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **otros)
        user.set_password(password)
        user.save()
        return user


class systemUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = systemAccountsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
