from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    """
    Данные по игре, когда началась и продолжается ли
    """
    created_ad = models.DateTimeField(auto_now_add=True)
    is_activate = models.BooleanField(default=True)
    game_key = models.CharField(max_length=8)

    class Meta:
        pass

    def __str__(self) -> str:
        return self.game_key


class Move(models.Model):
    """
    Ход игры
    """
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE)
    player = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    row = models.SmallIntegerField()
    col = models.SmallIntegerField()
    symbol = models.CharField(max_length=1)
    date_add = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата')

    def __str__(self) -> str:
        return f'{self.row} {self.col}'
