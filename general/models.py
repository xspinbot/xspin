from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено время", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", null=True, 
                                    blank=True, default=True)
    
    class Meta:
        abstract = True