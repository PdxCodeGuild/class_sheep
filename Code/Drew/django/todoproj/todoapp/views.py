from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem
from django.utils import timezone

def index(request):
    context = {
        'todos': ToDoItem.objects.filter(completed=False),
        'completed': ToDoItem.objects.filter(completed=True)
    }
    return render(request, 'todoapp/index.html', context)

def save_todo(request):
    print(request.POST)
    todo_text = (request.POST['todo_text'])
    todo_item = ToDoItem(todo_text=todo_text, completed_date=timezone.now(), completed=False)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

def complete_todo(request):
    print(request.POST)
    todo_id = request.POST['todo_id']
    todo_item = ToDoItem.objects.get(id=todo_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
