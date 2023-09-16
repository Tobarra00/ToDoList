from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Tasks(models.Model):
    
    task_title = models.CharField(max_length=50, null=False, blank=False)
    task_info = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task_info
    
    class Meta:
        db_table = 'Tasks'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'