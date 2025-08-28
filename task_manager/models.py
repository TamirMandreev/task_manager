import uuid

from django.db import models

# Create your models here.

class Task(models.Model):
    '''
    Модель "Задача". Содержит всю необходимую информацию о конкретной задаче.
    '''

    STATUS_CHOICES = [
        ('CREATED', 'Создано'),
        ('IN_PROGRESS', 'В работе'),
        ('COMPLETED', 'Завершено'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Название задачи', help_text='Укажите название задачи')
    description = models.TextField(verbose_name='Описание задачи', blank=True, null=True, help_text='Укажите описание задачи')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

