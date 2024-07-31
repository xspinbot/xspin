from django.db import models

from general.models import BaseModel
from general.choices import TransferType

from users.models import User, Admin
from groups.models import Group

# Create your models here.
class Transfer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Пользователь", related_name='user_transfers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name="Пользователю", related_name='to_user_transfers')
    chat = models.ForeignKey(Group, on_delete=models.CASCADE,
                             verbose_name="Чат")
    amount = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.user.name} -> {self.to_user.name} | {self.amount}"
    
    class Meta:
        verbose_name = "Трансфер"
        verbose_name_plural = "Трансферы"

class TransferAdmin(BaseModel):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,
                              verbose_name="Админ")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name="Пользователю")
    chat = models.ForeignKey(Group, on_delete=models.CASCADE,
                             verbose_name="Чат")
    transfer_type = models.CharField(max_length=255, choices=TransferType.choices,
                                     verbose_name="Тип трансфера")
    amount = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.admin.user.name} -> {self.to_user.name} | {self.amount}"
    
    class Meta:
        verbose_name = "Трансфер (Админ)"
        verbose_name_plural = "Трансферы (Админ)"