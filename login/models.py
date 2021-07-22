from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=15)
    password=models.CharField(max_length=10)
    repassword=models.CharField(max_length=10)



