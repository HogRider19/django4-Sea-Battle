from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Модель игры"""
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=10)
    player1 = models.OneToOneField(
        User, related_name='game', on_delate=models.DO_NOTHING)
    player2 = models.OneToOneField(
        User, related_name='game', on_delate=models.DO_NOTHING)
    spectators = models.ManyToManyField(
        User, related_name='viewed_game', on_delate=models.DO_NOTHING())
    subscribers = models.ManyToManyField(
        User, related_name='viewed_game', on_delate=models.DO_NOTHING())
    create_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
