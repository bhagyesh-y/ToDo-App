from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
      list_display=("task_name","is_completed","updated_at")
      search_fields=("task_name",)
admin.site.register(Task,TaskAdmin)

