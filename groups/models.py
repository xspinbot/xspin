from django.db import models
from general.models import BaseModel

# Create your models here.
class Group(BaseModel):
    chat_id = models.BigIntegerField(verbose_name="ID чата")
    invite_link = models.URLField(verbose_name="Ссылка для приглашения в чат", 
                                       null=True, unique=True)
    username = models.CharField(max_length=255, null=True, unique=True,
                                     verbose_name="Ссылка на чат")
    name = models.CharField(null=True, max_length=255,
                            verbose_name="Имя чата")
    
    def __str__(self):
        return f"{self.name} | {self.chat_id}"

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
    