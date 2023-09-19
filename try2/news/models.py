from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200) 
    description=models.TextField(blank=True)                      
    image=models.ImageField(upload_to='images/')
                       
    @property
    def limit_description(self):
        return self.description[:200] + '...'                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                        