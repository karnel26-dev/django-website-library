from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Фото профиля'),
    phone = models.CharField(max_length=20, verbose_name="Телефон"),
    city = models.CharField(max_length=30, verbose_name="Город"),
    birthday = models.DateTimeField(verbose_name="Дата рождения")