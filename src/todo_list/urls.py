from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'todo_list'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='todo_list/index.html')),
    path('', views.mainApp, name='mainApp'),
]
