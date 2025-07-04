from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib import messages

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Employee added successfully!")
            return redirect('employee_add')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/add_employee.html', {'form': form})
