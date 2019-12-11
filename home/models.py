from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='images/', null=True, verbose_name="")
    breed = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    favourite_food = models.CharField(max_length=50)
    like = models.IntegerField(default=0)

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name="owner")

    father = models.ForeignKey('Dog', on_delete=models.CASCADE, blank=True, null=True, related_name="Dad")
    mother = models.ForeignKey('Dog', on_delete=models.CASCADE, blank=True, null=True, related_name="Mom")
    
    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={'pk', self.pk})
        
    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    msg = models.TextField(max_length=200)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name