from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def buku(request):
    
    judul = ["Belajar Django","Belajar Javascript","Belajar HTML CSS","Belajar PHP"]
    penulis = "Aries Dimas"

    data = {
        "title":judul,
        "writer":penulis
    }

    return render(request, "buku.html",data)

def penerbit(request) :
    
    penerbit = ["Yudhistira"]
   

    data = {
       "writer":penerbit
    }

    return render(request, "penerbit.html",data)
