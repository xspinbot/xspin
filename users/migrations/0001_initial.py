# Generated by Django 5.0.7 on 2024-07-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('user_id', models.BigIntegerField(null=True, unique=True, verbose_name='ID пользователя')),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='ID пользователя')),
                ('name', models.CharField(max_length=320, null=True, verbose_name='Имя')),
                ('balance', models.IntegerField(default=0, verbose_name='Баланс')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Запрещен')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
