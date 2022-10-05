from django.urls import path
from . import views

urlpatterns = [
    path('gamelist/', views.GameListView.as_view(), name='gamelist'),
    path('', views.HomeView.as_view(), name='home'),
]