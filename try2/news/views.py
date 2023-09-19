from django.shortcuts import render
from .models import blog

# Create your views here.
def index(request):
    data={
        'blogsData':blog.objects.all()
    }
    return render(request,'index.html',data)


def details(request,slug):
    data={
        'blog': blog.objects.get(slug=slug)
    }
    return render(request,'details.html' , data)

def contact(request):
    return render(request,'contact.html')

