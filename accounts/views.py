from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "🎉 Logged in successfully!")
            return redirect('dashboard')  # your dashboard url name
        else:
            messages.error(request, "⚠️ Invalid username or password.")

    return render(request, "accounts/login.html")


def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

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
