from django.db import models
from django.conf import settings


class Folder(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    deleted = models.BooleanField(default="false")


class Task(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    deleted = models.BooleanField(default="false")
    folder_id = models.ForeignKey(
        to=Folder, null="true", on_delete=models.CASCADE
    )
