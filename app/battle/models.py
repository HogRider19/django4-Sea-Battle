from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Модель игры"""
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=10)
    battle_map = models.CharField(max_length=500)
    winner = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    player1 = models.OneToOneField(
        User, related_name='game', on_delete=models.DO_NOTHING)
    player2 = models.OneToOneField(
        User, related_name='game', on_delete=models.DO_NOTHING)
    spectators = models.ManyToManyField(User, related_name='viewed_game')
    subscribers = models.ManyToManyField(User, related_name='viewed_game')
    create_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    finished_at = models.DecimalField()

    def __str__(self) -> str:
        return self.name
