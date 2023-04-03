from .models import Folder, Task
from rest_framework import serializers
from django.contrib.auth.models import User
# Serializers define the API representation.


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Folder
        fields = ['user_id', 'title', 'deleted']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title',
                  'deleted', 'completed']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']
