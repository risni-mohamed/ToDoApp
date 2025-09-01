from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'welcome'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

def welcome(request):
    return render(request, "todo/welcome.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "todo/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "todo/login.html")

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(user=request.user, title=title)
        return redirect("task_list")

    return render(request, "todo/task_list.html", {"tasks": tasks})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect("task_list")

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect("task_list")
