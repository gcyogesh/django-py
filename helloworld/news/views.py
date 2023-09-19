from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(requests):
    data={
        'students':Student.objects.all()
    }
    return render(requests,'index.html',data)
    
def about(requests):
    return render(requests,'about.html')

def hero(requests):
    return render(requests,'hero.html')
    
def insert(request):
    if request.method == 'POST':
        name=request.POST
        
    else:
        return render(request,'insert.html')   
   
   