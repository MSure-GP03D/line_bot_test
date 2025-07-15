# Create your models here.
# main/models.py
from django.db import models

class User(models.Model):
    firebase_uid = models.CharField(max_length=255, unique=True)
    line_user_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class ActionItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.assigned_to.name}"