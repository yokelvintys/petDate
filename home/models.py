from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='images/', null=True, verbose_name="")
    breed = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    favourite_food = models.CharField(max_length=50)
    like = models.IntegerField(default=0)

    owner_name = models.CharField(max_length=50)
    owner_contact_info = models.TextField(max_length=50)

    father = models.ForeignKey('Dog', on_delete=models.CASCADE, blank=True, null=True, related_name="Dad")
    mother = models.ForeignKey('Dog', on_delete=models.CASCADE, blank=True, null=True, related_name="Mom")
    
    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={'pk', self.pk})
        
    def __str__(self):
        return self.name