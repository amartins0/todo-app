from rest_framework import serializers
from .models import Tarefa


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
