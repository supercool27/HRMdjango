from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

def employee_directory_path(instance, filename):
    folder_name = slugify(instance.user.email.split('@')[0]) if instance.user.email else f"user_{instance.user.id}"
    return f'employees/{folder_name}/{filename}'

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # models.py (Employee class ke andar)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)


    # Basic
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to=employee_directory_path, blank=True, null=True)

    # Official
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    employment_type = models.CharField(max_length=20, choices=[("Permanent", "Permanent"), ("Contract", "Contract"), ("Intern", "Intern")])
    work_location = models.CharField(max_length=100)
    reporting_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reportees')
    status = models.CharField(max_length=20, choices=[("Active", "Active"), ("Resigned", "Resigned"), ("Notice", "Notice")], default="Active")

    # Personal
    marital_status = models.CharField(max_length=10, choices=[("Single", "Single"), ("Married", "Married")])
    blood_group = models.CharField(max_length=5, blank=True)
    aadhaar_number = models.CharField(max_length=12, blank=True)
    pan_number = models.CharField(max_length=10, blank=True)
    passport_number = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=30, default='Indian')

    # Address
    current_address = models.TextField()
    permanent_address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    # Bank Details
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)

    # Education & Experience
    highest_qualification = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    total_experience = models.DecimalField(max_digits=4, decimal_places=1)
    previous_company = models.CharField(max_length=100, blank=True)
    previous_designation = models.CharField(max_length=100, blank=True)

    # Files
    resume = models.FileField(upload_to=employee_directory_path, blank=True)
    id_proof = models.FileField(upload_to=employee_directory_path, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"

