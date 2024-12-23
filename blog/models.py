from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Published_Date = models.DateTimeField(auto_now_add=False , null=True)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name='blogs')
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    