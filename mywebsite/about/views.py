from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        'judul':'Kelas Statik',
        'sub':'Halaman About',
        'banner':'img/about_banner.jpg'
    }

    return render(request, 'about.html', context)