from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveRequest, LeaveType
from .forms import LeaveRequestForm, LeaveTypeForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user
            leave.save()
            return redirect('leave_requests')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave/apply_leave.html', {'form': form})


def leave_requests(request):
    leaves = LeaveRequest.objects.filter(employee=request.user).order_by('-start_date')
    paginator = Paginator(leaves, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'leave/my_leaves.html', {'page_obj': page_obj})

def leave_types(request):
    types = LeaveType.objects.all()
    return render(request, 'leave/leave_types.html', {'types': types})

def leave_reports(request):
    all_leaves = LeaveRequest.objects.select_related('employee', 'leave_type').order_by('-start_date')

    paginator = Paginator(all_leaves, 10)  # 10 leave records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'leave/leave_reports.html', {
        'page_obj': page_obj,
    })


def leave_type_list(request):
    query = request.GET.get('q', '')
    leave_types = LeaveType.objects.filter(name__icontains=query).order_by('-id')
    paginator = Paginator(leave_types, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'leave/leave_type_list.html', {
        'page_obj': page_obj,
        'query': query
    })

def leave_type_create(request):
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave Type created successfully.")
            return redirect('leave_type_list')
    else:
        form = LeaveTypeForm()
    return render(request, 'leave/leave_type_form.html', {'form': form})


def leave_type_edit(request, pk):
    leave_type = get_object_or_404(LeaveType, pk=pk)
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST, instance=leave_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave type updated.")
            return redirect('leave_type_list')
    else:
        form = LeaveTypeForm(instance=leave_type)
    return render(request, 'leave/leave_type_form.html', {'form': form})


def leave_type_delete(request, pk):
    leave_type = get_object_or_404(LeaveType, pk=pk)
    leave_type.delete()
    messages.warning(request, "Leave type deleted.")
    return redirect('leave_type_list')