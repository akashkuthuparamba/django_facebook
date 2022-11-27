from django.db import models

# Create your models here.

class Log_in(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=30,default=None)
    last_name=models.CharField(max_length=30,default=None)
    email=models.EmailField(default=None)
    phone_no=models.IntegerField(default=None)
    education=models.TextField(default=None)
    place=models.CharField(max_length=80,default=None)


class Profile(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_no=models.IntegerField()