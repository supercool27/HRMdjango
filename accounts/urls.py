from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

urlpatterns = [
    # path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
    path('login/',views.login_view, name='login'),
]
