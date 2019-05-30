from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
import datetime

def index(request):
    context = {
        'message': 'Todo List!',
        'todos_incomplete': TodoItem.objects.filter(completed=False),
        'todos_completed': TodoItem.objects.filter(completed=True),
    }
   	
    return render(request, 'todoapp/index.html', context)


def save_todo(request):
    print(request.POST)
    todo_text = request.POST['cow']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index')) #lookup URL so it's not hard coded

def completed_todo(request, id_num):
	data_row = TodoItem.objects.get(id=id_num)
	print(data_row.completed)
	data_row.completed = True
	data_row.completed_date=datetime.datetime.now()
	data_row.save()
	return HttpResponseRedirect(reverse('todoapp:index'))