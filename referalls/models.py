from django.db import models
from general.models import BaseModel
from users.models import User

# Create your models here.
class Referall(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
        related_name="user_referalls", verbose_name="Пользователь")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, 
        related_name="from_user_referalls", verbose_name="От пользователя")
    
    def __str__(self):
        return f"{self.from_user} -> {self.user}"
    
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"