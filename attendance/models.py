from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='attendance_employee')
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

