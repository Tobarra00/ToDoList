from django.contrib import admin
from . import models

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task_info', 'user')
    
admin.site.register(models.Tasks, TasksAdmin)