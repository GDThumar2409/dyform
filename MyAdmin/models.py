from django.db import models

# Create your models here.

class Form(models.Model):
    Id = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=100,default='',unique=True)

class Textfield(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    form = models.ForeignKey(Form,on_delete=models.CASCADE)

