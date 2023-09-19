
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('insert',views.insert,name='insert'),
    path('about',views.about),
    path('hero',views.hero),
 
    
]


