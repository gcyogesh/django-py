
from django.urls import path
from .import views

urlpatterns = [
    
   path('',views.StudentListView.as_view(),name='index'),
   path('create',views.StudentCreateView.as_view(),name='create'),
   path('show',views.show, name='show'),
]
