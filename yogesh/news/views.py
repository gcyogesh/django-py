from django.shortcuts import render
from .models import hero
# Create your views here.

def index(request):
    data={
        'heroData':hero.objects.all()
    }
    return render(request,'index.html')

def details(slug ,request):
    data={
        'heroData':hero.objects.get(slug=slug)
    }
    return render(request,'details.html')

    