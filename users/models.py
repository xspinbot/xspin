from django.db import models
from general.models import BaseModel
from general.choices import LanguageType, AdminType

# Create your models here.
class User(BaseModel):
    user_id = models.BigIntegerField(unique=True, null=True, verbose_name="ID пользователя")
    username = models.CharField(max_length=255, unique=True,
                                null=True, blank=True, 
                                verbose_name="Имя пользователя")
    language = models.CharField(max_length=255, 
                                default=LanguageType.ru,
                                choices=LanguageType.choices)
    name = models.CharField(max_length=320, null=True, verbose_name="Имя")
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    transfer_limit = models.IntegerField(default=0, verbose_name="Дневной лимит трансфера")
    transfer_level = models.IntegerField(default=1, verbose_name="Уровень лимита трансфера")
    is_banned = models.BooleanField(default=False, verbose_name="Запрещен")

    def __str__(self):
        return f"{self.name} | {self.user_id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Admin(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    level = models.CharField(max_length=255, choices=AdminType.choices,
                             verbose_name="Уровень администратора")
    
    def __str__(self):
        return f"{self.user.name} | {self.user.user_id}"
    
    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"