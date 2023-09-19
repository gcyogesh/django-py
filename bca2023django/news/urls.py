from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('join', views.join),
    path('hero', views.hero),
]






