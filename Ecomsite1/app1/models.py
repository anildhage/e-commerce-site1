from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.
class Phone(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images')