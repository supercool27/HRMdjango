from django.db import models
from django.conf import settings

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status_choices = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected')
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type.name} ({self.status})"
