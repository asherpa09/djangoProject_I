from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    firstName = models.CharField(max_length=18)
    lastName = models.CharField(max_length=45)
    notes = models.TextField()
    myBooks = models.ManyToManyField(Book, related_name="myAuthors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

