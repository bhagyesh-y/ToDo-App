from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_name