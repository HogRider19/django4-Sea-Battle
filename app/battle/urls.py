from django.urls import path
from . import views
from . import ajaxviews

urlpatterns = [
    path('gamelist/', views.GameListView.as_view(), name='gamelist'),
    path('game/<int:pk>', views.GameDetailView.as_view() ,name='game'),
    path('', views.HomeView.as_view(), name='home'),

    path('gamefilter/', views.GameListFilter.as_view(), name='gamefilter'),
]