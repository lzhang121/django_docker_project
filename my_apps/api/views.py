import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.auth import authenticate, login


@csrf_exempt  # 实际部署时应使用 csrf_token 或 token 验证
def auth_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        return redirect('index.html')  # 登录成功跳转
    else:
        return render(request, 'login.html', {})


@csrf_exempt
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


@csrf_exempt
def user_view(request, action):
    """
    A simple view to handle login.
    """
    context = {
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    if request.method == 'POST':
        # Handle login logic here
        context["page_title"] = "Post request {}".format(action)
        return render(request, 'login.html', context)


@login_required(login_url='/auth/')
def user_dashboard(request):
    render(request, 'dashboard.html', {
        'current_time': now().strftime("%Y-%m-%d %H:%M:%S")
    })
