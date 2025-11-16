from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Book Shelf!")

def book_list(request):
    return render(request, 'raise_exception', "books")