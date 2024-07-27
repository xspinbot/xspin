# Generated by Django 5.0.7 on 2024-07-24 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0003_alter_group_invite_link_alter_group_username'),
        ('users', '0003_user_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('game', models.CharField(choices=[('basketball', 'Баскетбол'), ('football', 'Футбол'), ('dart', 'Дарт'), ('game_die', 'Игровой кубик'), ('bowling', 'Боулинг'), ('slot_machine', 'Игровой автомат')], max_length=255, verbose_name='Игра')),
                ('bid', models.IntegerField(verbose_name='Ставка')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Чат ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'История игры',
                'verbose_name_plural': 'История игры',
            },
        ),
    ]
