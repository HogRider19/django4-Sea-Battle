from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'player1', 'player2', 'start_at', 'finished_at']


admin.site.register(Game, GameAdmin)

