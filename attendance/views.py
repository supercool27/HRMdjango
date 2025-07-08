from django.shortcuts import render, redirect
from .forms import AttendanceForm
from django.contrib import messages
from .models import Attendance
from datetime import datetime, timedelta
from .models import Attendance, Employee
import calendar
from django.core.paginator import Paginator

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "✅ Attendance marked successfully!")
            except:
                messages.warning(request, "⚠️ Attendance for this employee and date already exists.")
            return redirect('mark_attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

def attendance_list(request):
    # Optional filter parameters
    employee_name = request.GET.get('employee')
    date = request.GET.get('date')

    attendances = Attendance.objects.all()

    # Filter if parameters are passed
    if employee_name:
        attendances = attendances.filter(employee__user__first_name__icontains=employee_name)

    if date:
        try:
            filter_date = datetime.strptime(date, "%Y-%m-%d").date()
            attendances = attendances.filter(date=filter_date)
        except ValueError:
            pass  # ignore invalid date format

    context = {
        'attendances': attendances.order_by('-date'),  # newest first
        'employee_name': employee_name,
        'date': date,
    }
    return render(request, 'attendance/attendance_list.html', context)


def attendance_report(request):
    selected_month = request.GET.get('month')
    today = datetime.today()

    if selected_month:
        year, month = map(int, selected_month.split('-'))
    else:
        year = today.year
        month = today.month

    start_date = datetime(year, month, 1).date()
    last_day = calendar.monthrange(year, month)[1]
    end_date = datetime(year, month, last_day).date()

    employees = Employee.objects.all()
    report_data = []

    for emp in employees:
        emp_row = {
            'employee': emp,
            'days': [],
            'present_count': 0,
            'absent_count': 0,
        }

        for day in range(1, last_day + 1):
            date = datetime(year, month, day).date()
            try:
                record = Attendance.objects.get(employee=emp, date=date)
                status = record.status
            except Attendance.DoesNotExist:
                status = '-'  # No data

            emp_row['days'].append(status)

            if status == 'P':
                emp_row['present_count'] += 1
            elif status == 'A':
                emp_row['absent_count'] += 1

        report_data.append(emp_row)

    # Paginate employees list
    paginator = Paginator(report_data, 5)  # Show 5 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'year': year,
        'month': month,
        'selected_month': f"{year}-{month:02d}",
        'days_range': range(1, last_day + 1),
    }
    return render(request, 'attendance/attendance_report.html', context)

