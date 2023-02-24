from django.shortcuts import render
from .models import Folder, Task


def mainApp(request):
    return render(
        request,
        'todo_list/index.html',
        {
            "folders": Folder.objects.filter(deleted=False),
            "in_folder_tasks": Task.objects.filter(deleted=False).exclude(folder_id__isnull=True),
            "lonely_tasks": Task.objects.filter(deleted=False).filter(folder_id__isnull=True),
        }
    )
