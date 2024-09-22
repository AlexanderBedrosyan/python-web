from django.shortcuts import render, HttpResponse
from .models import ToDoList

# Create your views here.


def home(request):
    all_tasks = None
    if request.GET.get('mybtn'):
        all_tasks = ToDoList.objects.all()
    tasks_content = {
        "tasks": all_tasks
    }

    return render(request, 'base.html', tasks_content)


def task_by_name(request, task_name):


    return HttpResponse(f"Task name is: {task_name}")


def custom_404(request, exception):
    return render(request, '404.html', status=404)