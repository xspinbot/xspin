from django.db import models
from general.models import BaseModel
from users.models import User

# Create your models here.
class Promocode(BaseModel):
    promocode = models.CharField(verbose_name="Промо-код", max_length=255, unique=True)
    cost = models.IntegerField(verbose_name="Цена")
    max_users = models.IntegerField(verbose_name="Максимальное количество пользователей")

    def __str__(self):
        return f"{self.promocode} | {self.cost}"
    
    class Meta:
        verbose_name = "Промо-код"
        verbose_name_plural = "Промокоды"

class UsedPromocode(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             verbose_name="Пользователь")
    promocode = models.ForeignKey(Promocode, on_delete=models.CASCADE,
                                  verbose_name="Промо-код")

    def __str__(self):
        return f"[ {self.promocode} ] [ {self.user} ]"
    
    class Meta:
        verbose_name = "Использованный промокод"
        verbose_name_plural = "Использованные промокоды"
