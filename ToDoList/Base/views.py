from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . import models, forms

# Create your views here.

class Register(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
        else:
            return render(request, 'register/register.html', {'form': form})
    
class Authenticate(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})
        
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')
        else: 
            messages.error(request, 'Wrong user and password')
            return render(request, 'login/login.html', {'form': form})
        
    
def close_session(request):
    
    logout(request)
    return redirect('base')


@login_required
def tasks(request):

    user_tasks = models.Tasks.objects.filter(user=request.user.id).order_by('-id')

    return render(request, 'task/task.html', {'user_tasks': user_tasks})

@login_required
def search(request):
    
    if request.method == 'POST':
        searched = request.POST.get('search')
        task_searched = models.Tasks.objects.filter(user=request.user.id, task_title__icontains=searched).order_by('-id')
        return render(request, 'task/task.html', {'user_tasks': task_searched})


@login_required
def new_task(request):
    
    if request.method == 'GET':
        form = forms.NewTask()
        return render(request, 'task/new_task.html', {'form': form})
    else:
        form = forms.NewTask(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            completed = form.cleaned_data.get('completed')
            user = request.user
            models.Tasks.objects.create(task_title=title, task_info=content, user=user, completed=completed)
            return redirect('base')
        else:
            return render(request, 'task/new_task.html', {'form': form})
        
@login_required
def edit_task(request, id):

    task_d = models.Tasks.objects.get(user=request.user.id, id=id)
    if request.method == 'GET':
        form = forms.NewTask(initial={'title': task_d.task_title, 'content': task_d.task_info, 'completed': task_d.completed}) 
        return render(request, 'task/edit_task.html', {'form': form})   
    else:
        form = forms.NewTask(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            completed = form.cleaned_data.get('completed')
            models.Tasks.objects.filter(user=request.user.id, id=id).update(task_title=title, task_info=content, completed=completed)
            return redirect('base')
        else:
            return render(request, 'task/edit_task.html', {'form': form})

@login_required
def remove_task(request, id):
    models.Tasks.objects.get(user=request.user.id, id=id).delete()
    return redirect('base')

    
    