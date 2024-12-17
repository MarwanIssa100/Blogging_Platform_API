from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, default="")
    profile_pic = models.ImageField(upload_to="profile_pics/" ,default="", blank=True , null=True) 
    
    def __str__(self):
        return self.username