# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from .forms import DepartmentForm

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'department/department_form.html', {'form': form})

def department_edit(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=dept)
    if form.is_valid():
        form.save()
        return redirect('department_list')
    return render(request, 'department/department_form.html', {'form': form})

def department_delete(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': dept})
