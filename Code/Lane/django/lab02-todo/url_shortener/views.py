from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlShortener
from django.utils.crypto import get_random_string

def index(request):
	urls = UrlShortener.objects.all()
	return render(request, 'url_shortener/index.html', {})

def save(request):
	print(request.POST)
	url_text = request.POST['url_box']
	data_row = UrlShortener(url=url_text, code=get_random_string(length=10))
	data_row.save()
	return HttpResponseRedirect(reverse('url_shortener:index'))


def test(request):
	print(get_random_string(length=32))
	data_row = UrlShortener.objects.get(code="hello")
	print(data_row)
	return (HttpResponseRedirect(f"Http://{data_row.url}"))

	# think twitter and their url shortener/character limits for posts when linking to another website



	'''

def save_todo(request):
    print(request.POST)
    todo_text = request.POST['cow']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index')) #lookup URL so it's not hard coded
'''