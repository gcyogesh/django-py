from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    data={
        'categoryData': Category.objects.all(),
    }
    return render(request,'pages/index.html', data)


def news(request):
    # send_mail("test", "kate haru gaf garchar", "ram@gmail.com", ["mern3pm@gmail.com"], fail_silently=False)

    if request.method == "POST":
        search = request.POST.get('search')
        n_data = News.objects.filter(title__icontains=search)
        paginator = Paginator(n_data, 50)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {
            'newsData':page_obj,
        }
        return render(request, 'pages/news.html', data)

    else:
        n_data = News.objects.all()
        paginator = Paginator(n_data, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {
            'newsData': page_obj,
        }
        return render(request, 'pages/news.html', data)




def news_details(request, slug):
    find_data = News.objects.get(slug=slug)
    cat_id = find_data.category_id
    related_news = News.objects.filter(category_id=cat_id).exclude(slug=slug)
    data = {
        'newsData':find_data,
        'relatedNews':related_news,
    }
    return render(request, 'pages/news_details.html', data)