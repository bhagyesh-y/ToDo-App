from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from testapp.models import Task
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages





# function for registering new user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Account created successfully")
            return redirect('home')
    else:
        form = RegisterForm()
            
    return render(request,'register.html',{'form':form})
        
        
        
# function for fetching data form db , rendering on frontend
@login_required
def Home(request):
    tasks = Task.objects.filter(
        user=request.user,
        is_completed=False).order_by('-updated_at') # order by will show data in ascending order and if passed as negative it will show in descending order
    #filter takes if condition as parameter for retrieving data from task model form db
    completed_tasks = Task.objects.filter(user=request.user,is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
        #sending key from here and receiving the key in html template to access the db fields via context dictionary
    }
    return render (request,'home.html',context)


# Function for adding data to db from frontend 
@login_required
def add_task(request):
    if request.method == 'POST':
       task_name = request.POST['task_name']
       task_desc = request.POST['task_desc']
       
       Task.objects.create(
           user =request.user,
           task_name=task_name,
           task_desc=task_desc
           )
       messages.success(request, "Task added successfully")
    return redirect ('home')


@login_required
def done_task(request,pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    # first pk is field name in task model and second pk is dynamic pk that we are passing
    task.is_completed= True
    task.save()
    messages.success(request,"Task marked as completed")
    return redirect('home')
    
    
@login_required    
def undone_task(request,pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    task.is_completed=False
    task.save()
    messages.info(request,"Task moved back to queue")
    return redirect('home')   


# function for updating the data
@login_required
def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk,user=request.user)
    if request.method == 'POST':
        new_task_name = request.POST['task_name']
        new_task_desc = request.POST['task_desc']
        get_task.task_name = new_task_name
        get_task.task_desc = new_task_desc
        get_task.save()
        messages.success(request,"Task updated successfully")
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)
    
    
    
    
# function for deleting the data
@login_required
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    task.delete()
    messages.info(request,"Task deleted")
    return redirect ('home')
            