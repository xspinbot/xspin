# Generated by Django 5.0.7 on 2024-07-29 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_alter_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_referalls', to='users.user', verbose_name='От пользователя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_referalls', to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
