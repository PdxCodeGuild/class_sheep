from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

# Create your views here.
def index(request):
    # html = '<html><head></head><body>'
    # html += '<ul>'
    # for i in range(10):
    #     html += '<li>' +str(i) + '</li>'
    # html += '</ul>'
    # html += '</body></html>'
    # return HttpResponse('ok')

    context = {
        'message': 'hello world',
        'todos': TodoItem.objects.all(),
    }
    print(context['todos'])
    return render(request, 'todoapp/index.html', context)

def view2(request):
    return HttpResponse('view 2')

def save_todo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

# def save_todo(request):
#     return HttpResponse('ok')
