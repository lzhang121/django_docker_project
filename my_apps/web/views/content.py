import datetime
from django.shortcuts import render


def content_view(request, cid):
    """
    Renders the content page.
    """

    context = {
        'page_title': f'Content Page {cid}',
        'message': f'This is the content for item {cid}.',
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    return render(request, 'content/index.html', context)
