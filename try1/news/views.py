from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def service(request):
    return render(request,'service.html')


def send_mail(request):
    return render(request,'email.html',
   { 'title': 'Send Mail'}
    
    )