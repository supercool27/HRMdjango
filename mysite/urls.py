from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("<h1>Welcome to Railway Django Deployment Mr. Manoj Pali Welcome in home !</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/', include('accounts.urls'))
]
