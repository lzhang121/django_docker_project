from django.urls import path, re_path
from . import views

urlpatterns = [
    path('auth/', views.auth_view, name='auth'),
    path('login/', views.login_view, name='login'),
    path('user/', ([
        path('add', views.user_view, name='add_user'),
        path('delete', views.user_view, name='delete_user'),
        path('edit', views.user_view, name='edit_user'),
        path('list', views.user_view, name='list_user'),
    ], None, None))
]
