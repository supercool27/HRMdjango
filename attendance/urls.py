from django.urls import path
from .views import mark_attendance,attendance_list,attendance_report

urlpatterns = [
    path('mark/', mark_attendance, name='mark_attendance'),
    path('view/', attendance_list, name='attendance_list'),
    path('report/', attendance_report, name='attendance_report'),

]
