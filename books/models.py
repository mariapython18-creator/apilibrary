from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=15)
    author=models.CharField(max_length=15)
    language= models.CharField(max_length=15)
    image = models.ImageField(upload_to="photos/")
    price=models.IntegerField()#