from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/')

    @property
    def limit_description(self):
        return self.description[:200] + '...'












