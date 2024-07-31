from django.contrib import admin
from referalls import models

# Register your models here.
@admin.register(models.Referall)
class ReferallAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'from_user', 'created_at')
    fields = ('user', 'from_user')
    search_fields = ('id', 'user', 'from_user', 'created_at')
