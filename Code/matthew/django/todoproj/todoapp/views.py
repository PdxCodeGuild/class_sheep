from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

import random

def index(request):
    # html = '<html><head></head><body>'
    # html += '<ul>'
    # for i in range(10):
    #     html += '<li>' + str(i) + '</li>'
    # html += '</ul>'
    # html += '</body></html>'
    # return HttpResponse(html)

    # div = '<div>'
    # for i in range(100):
    #     div += str(random.randint(1,10)) + ','
    # div += '</div>'

    context = {
        'message': 'Todo List',
        'todos': TodoItem.objects.all()
    }

    return render(request, 'todoapp/index.html', context)


def view2(request):
    return HttpResponse('You\'re at view2')


def save_todo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


# def save_todo(request):
#     return HttpResponse('ok!')
