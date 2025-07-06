from django.urls import path
from .views import add_employee,employee_list
from . import views

urlpatterns = [
    path('add/',add_employee, name='employee_add'),
    path('list/',employee_list, name='employee_list'),
    path('<int:pk>/edit/', views.edit_employee, name='employee_edit'),
    path('<int:pk>/delete/', views.delete_employee, name='employee_delete')
]