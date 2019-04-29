from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.utils import timezone

def index(request):
    context = {
        'todos': TodoItem.objects.filter(completed=False),
        'todos_completed': TodoItem.objects.filter(completed=True)
    }
    return render(request, 'todoapp/index.html', context)


# def view2(request):
#     return HttpResponse('ok')

# Create your views here.

def save_todo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

# def delete_todo(request, todo_id):
#     todo_id = request.POST['todo_id']
#     todo_item = TodoItem.objects.get(pk=todo_id)
#     todo_item.delete()
#     return HttpResponseRedirect(reverse('todoapp:index'))

def complete_todo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.complete()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
