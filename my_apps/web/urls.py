from django.urls import path, re_path
from . import views

app_name = 'app'  # This is good practice for namespacing

urlpatterns = [
    # This maps the root of the app to home_view
    path('', views.home_view, name='index'),
    path('content_int/<int:cid>/', views.content_view, name='content_int'),
    path('content_str/<str:cid>/', views.content_view, name='content_str'),
    path('content_slug/<slug:cid>/', views.content_view, name='content_slug'),
    path('content_uuid/<uuid:cid>/', views.content_view, name='content_uuid'),
    path('content_path/<path:cid>/', views.content_view, name='content_path'),
    path('article/', views.article, name='article'),
    path('about/', views.about_view, name='about'),
    re_path(r'^content/(?P<cid>[\w-]+)/$',
            views.content_view, name='content_regex'),
    re_path(r'^keyword/(?P<cid>[\w-]+)/(?P<extra>\d+)/$',
            views.keyword, name='keyword_regex'),
]
