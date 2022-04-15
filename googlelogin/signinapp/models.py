from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)


class history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    search_content = models.TextField()
    
    def __str__(self) -> str:
        return str(self.user.username)