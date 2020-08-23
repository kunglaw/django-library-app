from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category

class Author(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    price = models.IntegerField(null=True) 
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title




