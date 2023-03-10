from rest_framework import serializers
from .models import Task




class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'deadline')

class TaskDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
