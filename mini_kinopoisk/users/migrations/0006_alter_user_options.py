# Generated by Django 5.0.7 on 2024-08-08 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
    ]