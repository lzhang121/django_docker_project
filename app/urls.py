from django.urls import path
from . import views

app_name = 'app'  # This is good practice for namespacing

urlpatterns = [
    # This maps the root of the app to home_view
    path('', views.home_view, name='index'),
]
