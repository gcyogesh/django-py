from django.urls import path
from .import views


urlpatterns = [
    path('',views.index, name='index'),
    path('news',views.news,name='news'),
    path('news-details/<slug>',views.news_details, name='news_details'),
]
 

 