from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from testapp.models import Task

# function for fetching data form db , rendering on frontend
def Home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # order by will show data in ascending order and if passed as negative it will show in descending order
    #filter takes if condition as parameter for retrieving data from task model form db
    completed_tasks = Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        #sending key from here and receiving the key in html template to access the db fields via context dictionary
    }
    return render (request,'home.html',context)


# Function for adding data to db from frontend 
def add_task(request):
    task_name = request.POST['task_name']
    task_desc = request.POST['task_desc']
    Task.objects.create(task_name=task_name,task_desc=task_desc)
    return redirect ('home')

def done_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    # first pk is field name in task model and second pk is dynamic pk that we are passing
    task.is_completed= True
    task.save()
    return redirect('home')
    
def undone_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')   

# function for updating the data
def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task_name = request.POST['task_name']
        new_task_desc = request.POST['task_desc']
        get_task.task_name = new_task_name
        get_task.task_desc = new_task_desc
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)
    
    
# function for deleting the data
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect ('home')
            