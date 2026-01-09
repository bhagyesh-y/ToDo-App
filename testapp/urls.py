from django.urls import path, include
from . import views

urlpatterns = [
    # Add Task
    path('add_task/',views.add_task ,name="add_task"),
    # Mark as Done
    path('done_task/ <int:pk>', views.done_task,name='done_task'),
    # Mark as Undone
    path('undone_task/<int:pk>',views.undone_task,name='undone_task'),
    # Edit
    path('edit_task/<int:pk>',views.edit_task,name='edit_task')
    
]
