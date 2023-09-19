from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    data={
        'blogsData':Blog.objects.all()
    }
    return render(request,'index.html',data)

def details(request, slug):
    data={
        'blog':Blog.objects.get(slug=slug)
    }
    return render(request,'details.html',data)


