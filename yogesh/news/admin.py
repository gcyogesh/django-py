from django.contrib import admin
from .models import hero
# Register your models here.

@admin.register(hero)
class blogAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    prepopulated_fields={'slug':['title']}
    
    