from django.contrib import admin
from groups import models

# Register your models here.
@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'username', 'name', 'created_at')
    search_fields = ('chat_id', 'username', 'name')
    fields = ('chat_id', 'invite_link', 'username', 'name')