from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('requests/', views.leave_requests, name='leave_requests'),
    path('reports/', views.leave_reports, name='leave_reports'),
    path('types/', views.leave_type_list, name='leave_type_list'),
    path('types/add/', views.leave_type_create, name='leave_type_create'),
    path('types/edit/<int:pk>/', views.leave_type_edit, name='leave_type_edit'),
    path('types/delete/<int:pk>/', views.leave_type_delete, name='leave_type_delete'),
]
