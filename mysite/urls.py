from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

def home(request):
    return HttpResponse("<h1>Welcome to Railway Django Deployment Welcome in home Brother !</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/', include('accounts.urls')),
    path('employees/', include('employees.urls')),  
    path('roles/', include('roles.urls')),
    path('department/', include('department.urls')),
    path('attendance/', include('attendance.urls')),
    path('leave/', include('leave.urls')),


    # Include employee URLs
    # path('employees/', include('employees.urls')),
    # path('attendance/', include('attendance.urls')),
    # path('leave/', include('leave.urls')),
    # path('payroll/', include('payroll.urls')),
    # path('recruitment/', include('recruitment.urls')),
    # path('performance/', include('performance.urls')),
    # path('training/', include('training.urls')),
    # path('documents/', include('documents.urls')),
    # path('settings/', include('settings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
