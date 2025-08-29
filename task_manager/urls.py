from django.urls import path

from task_manager import views

app_name = "task_manager"

urlpatterns = [
    path("create/", views.TaskCreateAPIView.as_view(), name="task-create"),
    path("list/", views.TaskListAPIView.as_view(), name="task-list"),
    path("<uuid:pk>/", views.TaskDetailAPIView.as_view(), name="task-detail"),
    path("update/<uuid:pk>/", views.TaskUpdateAPIView.as_view(), name="task-update"),
    path("delete/<uuid:pk>/", views.TaskDeleteAPIView.as_view(), name="task-delete"),
]
