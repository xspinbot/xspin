from django.contrib import admin
from promocodes import models

# Register your models here.
@admin.register(models.Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'promocode', 'cost', 'max_users', 'created_at')
    fields = ('promocode', 'cost', 'max_users')
    search_fields = ('id', 'promocode', 'cost', 'max_users', 'created_at')

@admin.register(models.UsedPromocode)
class UsedPromocodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'promocode', 'created_at')
    fields = ('user', 'promocode')
    search_fields = ('id', 'user', 'promocode', 'created_at')