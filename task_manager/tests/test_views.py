import pytest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from task_manager.models import Task


@pytest.fixture
def api_client():
    return APIClient()


class TestTaskAPI:

    @pytest.fixture
    def tasks(self):
        Task.objects.create(name="test1", description="description1")
        Task.objects.create(name="test2", description="description2")

    @pytest.fixture
    def pk_task(self):
        """
        Первичный ключ первой тестовой задачи
        """
        return Task.objects.get(name="test1").pk

    @pytest.mark.django_db
    def test_create_task(self, api_client):
        """
        Тестирует создание задачи
        """
        data = {
            "name": "test",
            "description": "test description",
        }
        response = api_client.post(
            reverse("task_manager:task-create"), data=data, format="json"
        )
        assert response.status_code == 201
        assert Task.objects.count() == 1
        assert Task.objects.get().name == "test"
        assert Task.objects.get().description == "test description"
        assert Task.objects.get().status == "CREATED"

    @pytest.mark.django_db
    def test_get_task_list(self, api_client, tasks):
        """
        Тестирует получение списка задач
        """
        response = api_client.get(reverse("task_manager:task-list"), format="json")
        assert response.status_code == 200
        assert len(response.data) == 2
        assert response.data[0]["name"] == "test1"

    @pytest.mark.django_db
    def test_get_task_detail(self, api_client, tasks, pk_task):
        """
        Тестирует получение одной задачи
        """

        response = api_client.get(
            reverse("task_manager:task-detail", args=(pk_task,)), format="json"
        )
        assert response.status_code == 200
        assert response.data["description"] == "description1"

    @pytest.mark.django_db
    def test_update_task(self, api_client, tasks, pk_task):
        """
        Тестирует обновление задачи
        """
        data = {"name": "test_update", "description": "test_update"}
        response = api_client.put(
            reverse("task_manager:task-update", args=(pk_task,)),
            data=data,
            format="json",
        )
        assert response.status_code == 200
        test = Task.objects.get(pk=pk_task)
        assert test.name == "test_update"
        assert test.description == "test_update"

    @pytest.mark.django_db
    def test_delete_task(self, api_client, tasks, pk_task):
        """
        Тестирует удаление задачи
        """
        response = api_client.delete(
            reverse("task_manager:task-delete", args=(pk_task,))
        )
        assert response.status_code == 204
        with pytest.raises(ObjectDoesNotExist):
            Task.objects.get(pk=pk_task)
