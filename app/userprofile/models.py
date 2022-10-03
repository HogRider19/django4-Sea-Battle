from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Профиль пользователя. Расширяет модель User"""
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.name
