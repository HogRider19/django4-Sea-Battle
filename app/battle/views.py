from django.shortcuts import render
from django.views.generic import View



class HomeView(View):
    """Домашняя страница"""
    def get(self, request, *args, **kwargs):
        return render(request, 'battle/home.html')
