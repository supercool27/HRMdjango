from django.shortcuts import render, get_object_or_404, redirect
from .models import Role
from .forms import RoleForm
from django.contrib import messages

# List View
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'roles/role_list.html', {'roles': roles})

# Create View
def role_create(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Role created successfully.")
            return redirect('role_list')
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = RoleForm()
    return render(request, 'roles/role_form.html', {'form': form})


# Edit View
def role_edit(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Role updated successfully.")
            return redirect('role_list')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/role_form.html', {'form': form})


# Delete View
def role_delete(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        messages.warning(request, f"🗑️ Role '{role.name}' has been deleted.")
        return redirect('role_list')
    return render(request, 'roles/role_confirm_delete.html', {'role': role})

