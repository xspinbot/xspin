from django.contrib import admin
from games import models

# Register your models here.
@admin.register(models.GameHistory)
class GameHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat', 'game', 'bid', 'is_won', 'created_at')
    search_fields = ('user', 'chat', 'game', 'bid', 'is_won')
    fields = ('user', 'chat', 'game', 'bid', 'is_won')