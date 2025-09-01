from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
