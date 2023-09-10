from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_game/', views.new_game, name='new_game'),
    path('game_board/<str:game_key>/', views.game_board, name='game_board'),
    path('make_move/', views.make_move, name='make_move'),
    path('get_moves/', views.get_moves, name='get_movies'),
]
