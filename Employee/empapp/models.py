from django.db import models

# Create your models here.
class Employee(models.Model):

  name=models.CharField(max_length=50)
  
  image=models.ImageField(upload_to="images",default="images/default1.jpg",blank=True)

  email=models.CharField(max_length=100)

  phone=models.PositiveIntegerField()

  address=models.CharField(max_length=200)

  post=models.CharField(max_length=100)

  salary=models.PositiveIntegerField()

def __str__(self):
    return self.name
