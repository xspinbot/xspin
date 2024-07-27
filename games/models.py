from django.db import models
from general.models import BaseModel
from general.choices import GameType
from groups.models import Group
from users.models import User

# Create your models here.
class GameHistory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    chat = models.ForeignKey(Group, on_delete=models.CASCADE,
                                verbose_name="Чат")
    game = models.CharField(max_length=255, choices=GameType.choices,
                            verbose_name="Игра")
    bid = models.IntegerField(verbose_name="Ставка")
    is_won = models.BooleanField(verbose_name="Выиграл")
    
    def __str__(self):
        return f"{self.game} | {self.user.name}"
    
    class Meta:
        verbose_name = "История игры"
        verbose_name_plural = "История игры"