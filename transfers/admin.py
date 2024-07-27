from django.contrib import admin
from transfers import models

# Register your models here.
@admin.register(models.Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'to_user', 'chat',  'amount', 'created_at')
    search_fields = ('user', 'to_user', 'chat',  'amount')
    fields = ('user', 'to_user', 'chat',  'amount')

@admin.register(models.TransferAdmin)
class TransferAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin', 'to_user', 'chat', 'transfer_type', 'amount', 'created_at')
    search_fields = ('admin', 'to_user', 'chat', 'transfer_type', 'amount')
    fields = ('admin', 'to_user', 'chat', 'transfer_type', 'amount')
