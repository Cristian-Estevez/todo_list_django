from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

app_name = 'todo_list'
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='todo_list/login.html',
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path('', views.mainApp, name='mainApp'),
    path('logout/', views.logout, name='logout'),
]
