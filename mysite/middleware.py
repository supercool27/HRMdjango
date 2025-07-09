from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

EXEMPT_URLS = [
    '/',
    '/accounts/login/',
    '/accounts/signup/',
    '/accounts/register/',
    '/admin/',
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        print(f'🧐 PATH: {path}, AUTH: {request.user.is_authenticated}')
        
        if not request.user.is_authenticated:
            if not any(path == url for url in EXEMPT_URLS):
                print(f'🔒 Redirecting to login for {path}')
                return redirect(settings.LOGIN_URL)
        return self.get_response(request)


