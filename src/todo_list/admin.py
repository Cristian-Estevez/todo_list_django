from django.contrib import admin
from .models import Folder, Task


class FolderAdmin(admin.ModelAdmin):
    list_display = ("title", "deleted",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "deleted",)


admin.site.register(Folder, FolderAdmin)
admin.site.register(Task, TaskAdmin)
