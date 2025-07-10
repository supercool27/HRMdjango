def is_hr_or_admin(user):
    return (
        user.is_authenticated and
        hasattr(user, 'employee') and
        user.employee.role and
        user.employee.role.name.lower() in ['admin', 'hr']
    )