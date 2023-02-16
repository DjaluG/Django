from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Statik',
        'sub':'Halaman Home',
        'banner':'img/home-banner.jpg'
    }
    return render(request,'index.html',context)