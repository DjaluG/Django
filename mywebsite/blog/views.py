from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'judul':'Kelas Statik',
        'sub':'Halaman About',
        'banner':'img/back.jpg'
    }
    return render(request, 'blog.html',context)