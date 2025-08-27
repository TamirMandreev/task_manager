from django.urls import path


import views

app_name = 'task_manager'

urlpatterns = [
    path('create/', views.TaskCreateAPIView.as_view(), name='task-create'),
    path('list/', views.TaskListAPIView.as_view(), name='task-list' ),
    path('<int:pk>/', views.TaskDetailAPIView.as_view(), name='task-detail'),
    path('update/<int:pk>/', views.TaskUpdateAPIView.as_view(), name='task-update'),
    path('delete/<int:pk>/', views.TaskDeleteAPIView.as_view(), name='task-delete'),
]