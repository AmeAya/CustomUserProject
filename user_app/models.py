from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)  # unique=True потому что email вместо username
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'email'  # Указываем поле которое необходимо для авторизации
    REQUIRED_FIELDS = []  # Указываем обязательные поля при регистрации/создании юзера

    objects = CustomUserManager()
