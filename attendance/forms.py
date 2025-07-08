from django import forms
from .models import Attendance, Employee

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
