from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView , UpdateView , DetailView 
from .models import *

# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name='index.html'
    # context_object_name='students'

    
class StudentCreateView(CreateView):
    model=Student 
    template_name='create.html'
    fields='__all__'
    
    success_url='/'
    
    
def show(request):
    students=Student.objects.all()
    return HttpResponse('i am,a the sdla')