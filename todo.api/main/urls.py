from django.urls import path
from . import views

urlpatterns = [
    # function urls
    # path('tasks/', views.tasks_list_create_view), # id не нужно GET запрос
    # path('tasks/<int:pk>/', views.task_detail_view), # id нужно GET
    # path('tasks-create/', views.task_create), # id не нужно POST запрос
    # path('tasks-update/<int:pk>', views.task_update), # id нужно PUT/PATCH
    # path('tasks-delete/<int:pk>', views.task_delete), # id нужно DELETE

    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
]

