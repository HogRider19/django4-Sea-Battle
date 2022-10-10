from django.shortcuts import render
from .models import Game
from django.http import JsonResponse
from django.views.generic import View, ListView, DetailView



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


class GameListFilter(View):
    def get(self, request, strslice):
        games = Game.objects.filter(name__icontains=strslice).values()
        return JsonResponse({'games': list(games)})


class GameDetailView(DetailView):
    model = Game
    template_name='battle/game.html'
