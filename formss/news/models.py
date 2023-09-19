from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=39)
    address=models.CharField(max_length=130)
    age=models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    
    
class Course(models.Model):
    name=models.CharField(max_length=100)    
    description=models.TextField()
    price=models.IntegerField()

    
    def __str__(self):
        return self.name
    
    
"""
create table news_student(
    id int primary key auto_increament,
    name varchar(100),
    email varchar(20),
    
)
"""    
    