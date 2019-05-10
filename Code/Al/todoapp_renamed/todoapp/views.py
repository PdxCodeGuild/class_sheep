from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem_models_py

import random

def index_views_fun(request):
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
        'message_views_dict': 'Todo List',
        'todos_views_dict': TodoItem_models_py.objects.all()
    }

    return render(request, 'todoapp/index.html', context)


def view2_views_fun(request):
    return HttpResponse('You\'re at view2')


def save_todo_views_fun(request):
    todo_text = request.POST['todo_text_input_html']
    todo_item = TodoItem_models_py(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp_urls_nickname:index_path_nickname'))


# def save_todo(request):
#     return HttpResponse('ok!')
