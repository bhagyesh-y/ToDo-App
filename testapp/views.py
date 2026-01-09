from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Task

def Home(request):
    tasks = Task.objects.filter(is_completed=False)
    #filter takes if condition as parameter for retrieving data from task model form db
    context={
        'tasks':tasks
        #sending key from here and receiving the key in html template to access the db fields via context dictionary
    }
    return render (request,'home.html',context)

def addTask(request):
    task_name = request.POST['task_name']
    task_desc = request.POST['task_desc']
    Task.objects.create(task_name=task_name,task_desc=task_desc)
    return HttpResponse('the form is submitted')