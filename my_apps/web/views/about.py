import datetime
from django.shortcuts import render


def about_view(request):
    """
    Renders the about page.
    """
    context = {
        'page_title': 'About Us',
        'message': 'This is the about page.',
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    return render(request, 'about/index.html', context)
