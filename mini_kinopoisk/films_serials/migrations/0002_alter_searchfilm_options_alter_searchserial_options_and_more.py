# Generated by Django 5.0.7 on 2024-08-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_serials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchfilm',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='searchserial',
            options={'verbose_name': 'Сериал', 'verbose_name_plural': 'Сериалы'},
        ),
        migrations.AlterField(
            model_name='searchfilm',
            name='picture',
            field=models.URLField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='searchserial',
            name='picture',
            field=models.URLField(max_length=350, null=True),
        ),
    ]
