from django.db import models

class Users(models.Model):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)  # 'admin', 'teacher'

class Tasks(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tasks')
    assigned_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_tasks')  # NEW
    priority = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20)  # 'pending', 'completed'
    created_at = models.DateTimeField(auto_now_add=True)