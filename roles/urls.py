from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='role_list'),
    path('add/', views.role_create, name='role_create'),
    path('<int:pk>/edit/', views.role_edit, name='role_edit'),
    path('<int:pk>/delete/', views.role_delete, name='role_delete'),
]
