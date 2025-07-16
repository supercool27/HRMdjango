# payroll/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendance_employee')
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)  # Optional if not used everywhere

    def __str__(self):
        return self.user.get_full_name()

class SalaryStructure(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic = models.FloatField()
    hra = models.FloatField()
    da = models.FloatField()
    other_allowances = models.FloatField()
    deductions = models.FloatField()
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

class SalaryAdjustment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    type = models.CharField(max_length=10, choices=[('Addition', 'Addition'), ('Deduction', 'Deduction')])
    amount = models.FloatField()
    reason = models.CharField(max_length=255)

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    gross = models.FloatField()
    deductions = models.FloatField()
    net = models.FloatField()
    generated_on = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='payslips/', null=True, blank=True)

# payroll/views.py
from django.shortcuts import render, get_object_or_404
from .models import SalaryStructure, SalaryAdjustment, Payslip, Employee
from datetime import date
from django.http import HttpResponse

def generate_payslip(request, employee_id, year, month):
    employee = get_object_or_404(Employee, id=employee_id)
    salary_structure = SalaryStructure.objects.filter(employee=employee).latest('effective_from')
    adjustments = SalaryAdjustment.objects.filter(employee=employee, month__year=year, month__month=month)

    gross = salary_structure.basic + salary_structure.hra + salary_structure.da + salary_structure.other_allowances
    total_deductions = salary_structure.deductions

    for adj in adjustments:
        if adj.type == 'Addition':
            gross += adj.amount
        else:
            total_deductions += adj.amount

    net = gross - total_deductions

    payslip = Payslip.objects.create(
        employee=employee,
        month=date(year, month, 1),
        gross=gross,
        deductions=total_deductions,
        net=net
    )

    return HttpResponse(f"Payslip generated: Net Salary = {net}")

# payroll/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-payslip/<int:employee_id>/<int:year>/<int:month>/', views.generate_payslip, name='generate_payslip'),
]

# payroll/admin.py
from django.contrib import admin
from .models import Employee, SalaryStructure, SalaryAdjustment, Payslip

admin.site.register(Employee)
admin.site.register(SalaryStructure)
admin.site.register(SalaryAdjustment)
admin.site.register(Payslip)

# settings.py (Add these to INSTALLED_APPS)
# 'payroll',

# Run these commands:
# python manage.py makemigrations payroll
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
