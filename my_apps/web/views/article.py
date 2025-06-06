import datetime
from django.shortcuts import render


def article_view(request):
    """
    Renders the about page.
    """
    aid = request.GET.get(
        'aid', None)  # Example of how to handle a query parameter if needed
    print(f"Article ID: {aid}")  # Debugging output
    context = {
        'page_title': 'Article',
        'message': "This is the article: {}".format(aid),
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    return render(request, 'about/index.html', context)


def keyword(request, cid, extra):
    """
    Renders the content page.
    """

    context = {
        'page_title': f'Content Page {cid} with Extra {extra}',
        'message': f'This is the content for item {cid} with extra {extra}.',
        # Add current time
        'current_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
    return render(request, 'content/index.html', context)
