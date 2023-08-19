from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('make_move/', views.make_move, name='make_move'),
]
