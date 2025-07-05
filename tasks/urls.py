# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('new/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]