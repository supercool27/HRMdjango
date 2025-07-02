from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model

def login_view(request):
    return render(request, 'accounts/login.html')


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')\

def signup_view(request):
    return render(request, 'accounts/signup.html')

def register_view(request):
    return render(request, 'accounts/successfull.html')

User = get_user_model()  

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        terms = request.POST.get("terms")

        context = {
            'name': name,
            'email': email,
        }
        
        if not all([name, email, password, terms]):
            messages.error(request, "⚠️ All fields are required.")
            return render(request, 'accounts/signup.html', context)

        if User.objects.filter(username=email).exists():
            messages.error(request, "⚠️ A user with this email already exists.")
            return render(request, 'accounts/signup.html', context)

    
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        messages.success(request, "🎉 Registration successful!")
        return render(request, 'accounts/successfull.html', {'name': name})

    return render(request, 'accounts/signup.html')


