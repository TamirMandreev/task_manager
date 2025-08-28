import pytest
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from task_manager.models import Task

@pytest.mark.django_db
def test_create_task():
    '''
    Тестирует создание задачи
    '''
    task = Task.objects.create(name='Первая задача', description='Это первая задача')
    assert task.name == 'Первая задача'
    assert task.description == 'Это первая задача'
    assert task.status == 'CREATED'


@pytest.mark.django_db
def test_create_task_empty_name():
    '''
    Тестирует создание задачи без названия
    '''
    with pytest.raises(ValidationError):
        Task.objects.create(name='')

