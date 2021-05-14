from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createBook', views.createBook, name="createBook"),
    path('authors', views.newAuthor),
    path('createAuthor', views.createAuthor),
    path('books/<int:bookId>', views.showBook),
    path('authors/<authorId>', views.showAuthor),
]
