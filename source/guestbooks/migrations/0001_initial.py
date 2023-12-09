# Generated by Django 5.0 on 2023-12-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('email', models.EmailField(max_length=60, verbose_name='Почта')),
                ('description', models.CharField(max_length=60, verbose_name='Описание')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('end_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], max_length=40, verbose_name='Статус')),
            ],
        ),
    ]
