import datetime
from django.shortcuts import render


def home_view(request):
    """
    Renders the homepage.
    """
    info = request.resolver_match
    if info.url_name not in ['index', 'home_view']:
        # If the URL name is not 'index' or 'home_view', redirect to home_view
        return render(request, 'home/index.html', {
            'page_title': 'Redirecting...',
            'message': 'no permission to access this page.',
            'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
        })
    else:
        context = {
            'page_title': 'Welcome to My Django Homepage',
            'message': 'Hello from Django! {}'.format(info),
            # Add current time
            'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
        }
        return render(request, 'home/index.html', context)
