from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from task_manager.models import Task
from task_manager.serializers import TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailAPIView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDeleteAPIView(DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
