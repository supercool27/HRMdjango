from django.shortcuts import get_object_or_404, render, redirect

from employees.models import Employee
from .forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator

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

def employee_list(request):
    query = request.GET.get('q')
    
    # Ensure only valid employees
    employees = Employee.objects.select_related('user').exclude(user__isnull=True)

    if query:
        employees = employees.filter(user__first_name__icontains=query)

    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/view_employee.html', {
        'page_obj': page_obj,
        'query': query,
    })

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Employee updated successfully.")
            return redirect('employee_edit', pk=employee.pk)
    return render(request, 'employee_update.html', {'form': form, 'employee': employee})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "🗑️ Employee deleted successfully.")
        return redirect('employee_list')  # You should define this list view
    return render(request, 'employee_confirm_delete.html', {'employee': employee})