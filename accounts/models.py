from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    designation = models.CharField(max_length=50,null=True, blank=True)
    user_image = models.ImageField(upload_to="../static/media")
    bio = models.TextField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)    
    mobile = models.CharField(max_length=20,default='+234')
    socialLinks = models.URLField(null=True,blank=True)

# class Guest(models.Model):
#     designation = models.CharField(max_length=50,null=True, blank=True)
#     user_image = models.ImageField(upload_to="../static/media")
#     bio = models.TextField(max_length=255,null=True,blank=True)
#     address = models.CharField(max_length=100,null=True,blank=True)
#     city = models.CharField(max_length=20,null=True,blank=True)







