from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoItem

# def index(request):
#     return HttpResponse('ok')

def index(request):
    context = {
        'message': 'hello world!',
        'todos': ToDoItem.objects.all()
    }
    return render(request, 'todoapp/index.html', context)

def save_todo(request):
    todo_text = (request.POST['todo_text'])
    todo_item = ToDoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
