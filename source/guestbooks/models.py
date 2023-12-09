from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Guest_books(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=60, null=False, blank=False, verbose_name='Почта')
    description = models.CharField(max_length=60, null=False, blank=False, verbose_name='Описание')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=40, null=False, blank=False, choices=status_choices, verbose_name='Статус')

    def __str__(self):
        return f'{self.pk}. {self.description}'