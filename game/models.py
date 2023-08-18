from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    """
    Данные по игре, когда началась и продолжается ли
    """
    created_ad = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)


class Move(models.Model):
    """
    Ход игры
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.IntegerField()
    col = models.IntegerField()
