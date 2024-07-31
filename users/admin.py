from django.contrib import admin
from users import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'username', 'name', 
                    'language', 'balance',
                    'transfer_limit', 'transfer_level',
                    'created_at', 'updated_at')
    search_fields = ('user_id', 'username', 'language', 'name', 
                     'balance', 'transfer_limit', 'transfer_level', 'is_banned')
    fields = ('user_id', 'username', 'language', 'name', 'balance', 
              'transfer_limit', 'transfer_level','is_banned')
    list_editable = ('balance', )


@admin.register(models.Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'level', 'created_at')
    search_fields = ('level', )
    fields = ('user', 'level')