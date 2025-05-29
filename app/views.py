import datetime
from django.shortcuts import render


def home_view(request):
    """
    Renders the homepage.
    """
    context = {
        'page_title': 'Welcome to My Django Homepage-docker',
        'message': 'Hello from Django!',
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    return render(request, 'home/index.html', context)
