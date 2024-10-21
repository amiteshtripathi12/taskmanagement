from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class Customuser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email

# Task model
class Task(models.Model):
    TASK_STATUS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='PENDING')
    assigned_users = models.ManyToManyField(Customuser, related_name='tasks')

    def __str__(self):
        return self.name
