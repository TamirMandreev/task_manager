from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from models import Task
from serializers import TaskSerializer


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