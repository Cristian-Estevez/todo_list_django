from django.db import models
from django.conf import settings


class Folder(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "id: {}; belongs to: {}, title: {}; deleted: {}".format(self.id, self.user_id, self.title, self.deleted)


class Task(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, serialize=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    folder_id = models.ForeignKey(
        to=Folder,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return """
                id: {}; 
                belongs to: {}, 
                title: {}; 
                deleted: {};
                in folder: {};
               """.format(
            self.id,
            self.user_id,
            self.title,
            self.deleted,
            self.folder_id
        )
