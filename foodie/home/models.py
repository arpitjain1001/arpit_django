from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your models here.
class Contact(models.Model):
    user=models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank= True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=12)
    desc=models.TextField()
    # date=models.DateField()
def __str__(self):
    return self.name