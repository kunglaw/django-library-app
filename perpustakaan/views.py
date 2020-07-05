from django.shortcuts import render
from django.http import HttpResponse

from perpustakaan.models import Book


# Create your views here.
def buku(request):
    
    # judul = ["Belajar Django","Belajar Javascript","Belajar HTML CSS","Belajar PHP"]
    # penulis = "Aries Dimas"
    books = Book.objects.all()

    data = {
       "books":books
    }

    return render(request, "buku.html",data)

def penerbit(request) :
    
    penerbit = ["Yudhistira"]
   

    data = {
       "writer":penerbit
    }

    return render(request, "penerbit.html",data)

def meme(request):
    return HttpResponse("meme")
