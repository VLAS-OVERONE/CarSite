# Generated by Django 3.2.5 on 2021-07-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Марка Автомобиля')),
                ('description', models.TextField(verbose_name='Описание автомобиля')),
            ],
        ),
    ]
