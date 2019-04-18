from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, TodoList
from django.utils import timezone


def todo_lists(request):
    todo_lists = TodoList.objects.all()
    context = {
        'todo_lists': todo_lists
    }
    return render(request, 'todoapp/todo_lists.html', context)

def index(request, todo_list_id):
    todo_list = TodoList.objects.get(pk=todo_list_id)
    print(TodoItem.objects.all())
    print(todo_list.items.all())
    # html = '<html><head></head><body>'
    # html += '<ul>'
    # for i in range(10):
    #     html += '<li>' + str(i) + '<li>'
    # html += '</body></html>'
    # return HttpResponse(html)
    context = {
        'todo_list': todo_list,
        'todos': todo_list.items.all()
    }

    return render(request, 'todoapp/index.html', context)

def save_todo_list(request):
    todo_list_id = request.POST['todo_list_id']
    todo_list = TodoList.objects.get(pk=todo_list_id)

def save_todo(request):
    todo_list_id = request.POST['todo_list_id']
    todo_list = TodoList.objects.get(pk=todo_list_id)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, list=todo_list)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

def delete_todo(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))

def complete_todo(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:detail', kwargs={'todo_list_id':todo_item.list.id}))

# def save_todo(request):
    # return HttpResponse('ok')
