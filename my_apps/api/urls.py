from django.urls import path, re_path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('login/', views.login_view, name='login'),
    # re_path(r'user/(?P<action>\w+)/?$', views.user_view, name='user'),
    path('user/<str:action>/', views.user_view, name='user_action'),
]
