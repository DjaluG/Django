from django.shortcuts import render
from multiprocessing import context
# Create your views here.

def contact(request):
    context ={
        'judul':'Kelas Statik',
        'sub':'Halaman Contact',
    }

    return render(request, 'contact.html', context)
