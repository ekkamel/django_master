from __future__ import unicode_literals  # makes database adapted to all languages
from django.db import models

# Create your models here.


class Main(models.Model):       # capital Main in order not to get confused with app name
      
    name = models.TextField()
    
    def __str__(self):
        return self.name 