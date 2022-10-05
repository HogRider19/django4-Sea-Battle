from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Модель игры"""
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    battle_map = models.CharField(max_length=500, blank=True, null=True)
    step_counter = models.PositiveIntegerField(default=0)
    winner = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    player1 = models.ForeignKey(
        User, related_name='game_player1', 
        on_delete=models.DO_NOTHING)
    player2 = models.ForeignKey(
        User, related_name='game_player2', 
        on_delete=models.DO_NOTHING, blank=True, null=True)
    spectators = models.ManyToManyField(
        User, related_name='viewed_game', blank=True)
    subscribers = models.ManyToManyField(
        User, related_name='signed_game', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
