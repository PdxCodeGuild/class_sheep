from django.shortcuts import render
from django.http import HttpResponse

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
        'message': 'hello world!',
        'todos': TodoItem.objects.all()
    }

    return render(request, 'todoapp/index.html', context)


def view2(request):
    return HttpResponse('You\'re at view2')
