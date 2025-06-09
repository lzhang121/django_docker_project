from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('about', views.about_required, name='about'),
    path('about', views.about_required, name='about'),
]
