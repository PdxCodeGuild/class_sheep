from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from .models import List, Todo
from django.utils import timezone

def index(request):
    latest_todo_lists = List.objects.order_by('-date_created')[:5]
    context = {
        'latest_todo_lists': latest_todo_lists,
    }
    return render(request, 'remake_todo/index.html', context)

def detail(request, list_id):
    todo_list = get_object_or_404(List, pk=list_id)
    context = {
        'todo_list': todo_list,
        'complete': todo_list.todos.filter(completed=True),
        'incomplete': todo_list.todos.filter(completed=False),
    }
    return render(request, 'remake_todo/detail.html', context)

def save_todo_list(request):
    todo_text = request.POST['todo_text']
    new_list = List(list_text = todo_text)
    new_list.save()
    return HttpResponseRedirect(reverse('remake_todo:index'))

def add_todo(request, list_id):
    list = List.objects.get(pk=list_id)
    todo_text = request.POST['todo_text']
    todo_item = Todo(todo_text=todo_text, list=list, completed=False)
    todo_item.save()
    return HttpResponseRedirect(reverse('remake_todo:detail', args=(list_id,)))

def mark_completed(request, list_id):
    todo_id = request.POST['todo_id']
    todo_item = Todo.objects.get(pk=todo_id)
    todo_item.date_completed = timezone.now()
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('remake_todo:detail', args=(list_id,)))

def mark_incomplete(request, list_id):
    todo_id = request.POST['todo_id']
    todo_item = Todo.objects.get(pk=todo_id)
    todo_item.completed = False
    todo_item.save()
    return HttpResponseRedirect(reverse('remake_todo:detail', args=(list_id,)))



# for todo_list in latest_todo_lists:
#     print(todo_list.id)
#     print(todo_list.list_text)
#     print(todo_list.date_created)
#     print()
