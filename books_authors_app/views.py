from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.all()
    context ={
        'books': books,
    }
    return render(request, 'index.html', context)

def createBook(request):
    if request.method == 'POST':
         Book.objects.create('title' = request.POST['title'],'description' = request.POST['description'],
         return redirect('/')
    return redirect('/')
    

def newAuthor(request):
    pass

def createAuthor(request):
    pass

def showBook(request):
    pass

def showAuthor(request):
    pass