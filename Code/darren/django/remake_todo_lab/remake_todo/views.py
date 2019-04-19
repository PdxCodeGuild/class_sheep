from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import List, Todo

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

def save_todo(request, list_id):
    response = "You're attempting to save your todo to list %s."
    return HttpResponse(response % list_id)


# for todo_list in latest_todo_lists:
#     print(todo_list.id)
#     print(todo_list.list_text)
#     print(todo_list.date_created)
#     print()
