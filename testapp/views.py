from django.shortcuts import redirect, render
from django.http import HttpResponse
from testapp.models import Task

def Home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # order by will show data in ascending order and if passed as negative it will show in descending order
    #filter takes if condition as parameter for retrieving data from task model form db
    completed_tasks = Task.objects.filter(is_completed = True)
    context={
        'tasks':tasks,
        'completed_task':completed_tasks
        #sending key from here and receiving the key in html template to access the db fields via context dictionary
    }
    return render (request,'home.html',context)

def addTask(request):
    task_name = request.POST['task_name']
    task_desc = request.POST['task_desc']
    Task.objects.create(task_name=task_name,task_desc=task_desc)
    return redirect ('home')