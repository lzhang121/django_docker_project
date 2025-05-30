import datetime
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # 实际部署时应使用 csrf_token 或 token 验证
def auth_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f"Username: {username}, Password: {password}")
    else:
        context = {
            'page_title': 'AuthPage',
            'message': 'Hello from Django!',
            'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        return render(request, 'auth.html', context)


def login_view(request):
    """
    A simple view to handle login.
    """
    if request.method == 'POST':
        # Handle login logic here
        return HttpResponse("Login successful")
    else:
        # Render an authentication form
        context = {
            'page_title': 'LoginPage',
            'message': 'Hello from Django!',
            # Add current time
            'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
        }
        return render(request, 'login.html', context)


def user_view(request):
    """
    A simple view to handle login.
    """
    if request.method == 'POST':
        # Handle login logic here
        return HttpResponse("Login successful")
    else:
        # Render an authentication form
        context = {
            'page_title': 'LoginPage',
            'message': 'Hello from Django!',
            # Add current time
            'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
        }
        return render(request, 'login.html', context)
