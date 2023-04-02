# Generated by Django 4.1.7 on 2023-04-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_folder_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
