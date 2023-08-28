from django.db import models

# Create your models here.
class Student_model(models.Model):
    name = models.CharField(max_length=10000)
    age = models.IntegerField()
    gender = models.CharField(max_length=1000)
    standard = models.IntegerField()
    address = models.CharField(max_length=10000,default="address")
    
