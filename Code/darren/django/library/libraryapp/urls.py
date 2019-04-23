from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'libraryapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/author_index/', views.author_index, name='author_index'),
    path('index/book_index/', views.book_index, name='book_index'),
    path('index/author_index/<int:author_id>/detail/', views.author_detail, name='author_detail'),
    path('index/book_index/<int:book_id>/detail/', views.book_detail, name='book_detail'),
    path('index/checkout/', views.checkout, name='checkout'),
]

# def index(request):
#     response = "You're looking at Index."
#     return HttpResponse(response)
#
# def author_index(request):
#     response = "You're looking at the authors page"
#     return HttpResponse(response)
#
# def author_detail(request, author_id):
#     response = "You're looking at author page %"
#     return HttpResponse(response % author_id)
#
# def book_index(request):
#     response = "You're looking at the books page"
#     return HttpResponse(response)
#
# def book_detail(request, book_id):
#     response = "You're looking at book page %"
#     return HttpResponse(response % book_id)
#
# def checkout(request):
#     return HttpResponse("You're voting on question %s." % question_id)
