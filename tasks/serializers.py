from rest_framework import serializers
from .models import Task, Customuser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, Customuser  
from .serializers import *
from rest_framework import generics



class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id', 'name', 'email', 'mobile']

# Task Serializer for task models 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users']

# User Serializer for task assignment to the users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id', 'name', 'email']


