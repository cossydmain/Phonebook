
from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Phonebook(models.Model):
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=20)
    emailaddress = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:index')



