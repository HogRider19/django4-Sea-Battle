from django.shortcuts import render
from .models import Game
from django.views.generic import View, ListView



class HomeView(View):
    """Домашняя страница"""
    def get(self, request, *args, **kwargs):
        return render(request, 'battle/home.html')


class GameListView(ListView):
    model = Game
    template_name = 'battle/gamelist.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.all()
