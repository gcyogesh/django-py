
from django.contrib import admin
from django.urls import path,include
from news.views import send_mail

urlpatterns = [
    path('',include('news.urls')),
    path('admin/', admin.site.urls),
    path('send/',send_mail,name='email')
]
