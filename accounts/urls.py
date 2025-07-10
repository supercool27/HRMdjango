from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

urlpatterns = [
    # path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout')
]
