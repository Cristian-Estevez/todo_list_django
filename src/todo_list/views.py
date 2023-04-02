from django.shortcuts import render, redirect
from .models import Folder, Task
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializers import FolderSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return render(request, 'mainApp')


def mainApp(request):
    if request.user.is_authenticated:
        return render(
            request,
            'todo_list/task_list.html',
            {
                "folders":
                    Folder.objects.filter(deleted=False)
                    .filter(user_id=request.user.id),
                "in_folder_tasks":
                    Task.objects
                    .filter(deleted=False)
                    .exclude(folder_id__isnull=True)
                    .filter(user_id=request.user.id),
                "lonely_tasks":
                    Task.objects.filter(deleted=False)
                    .filter(folder_id__isnull=True)
                    .filter(user_id=request.user.id),
            }
        )
    else:
        return render(
            request,
            'todo_list/task_list.html',
            {
                "folders":
                    Folder.objects.filter(deleted=False)
                    .filter(user_id__isnull=True),
                "in_folder_tasks":
                    Task.objects.filter(deleted=False)
                    .exclude(folder_id__isnull=True)
                    .filter(user_id__isnull=True),
                "lonely_tasks":
                    Task.objects.filter(deleted=False)
                    .filter(folder_id__isnull=True)
                    .filter(user_id__isnull=True),

            }
        )


# ViewSets define the view behavior.
class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
