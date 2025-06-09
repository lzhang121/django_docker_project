from django.urls import path, re_path
from .views import about
from .views import article
from .views import content
from .views import home

app_name = 'app'  # This is good practice for namespacing

urlpatterns = [
    # This maps the root of the app to home_view
    path('', home.home_view, name='index'),
    path('content_int/<int:cid>/', content.content_view, name='content_int'),
    path('content_str/<str:cid>/', content.content_view, name='content_str'),
    path('content_slug/<slug:cid>/', content.content_view, name='content_slug'),
    path('content_uuid/<uuid:cid>/', content.content_view, name='content_uuid'),
    path('content_path/<path:cid>/', content.content_view, name='content_path'),
    path('article/', article.article_view, name='article'),
    path('about/', about.about_view, name='about'),
    re_path(r'^content/(?P<cid>[\w-]+)/$',
            content.content_view, name='content_regex')
]
