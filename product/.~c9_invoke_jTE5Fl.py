from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    seat = models.TextField()
    time = models.CharField(max_length=200)
    
    null = True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    seat = models.TextField()
    time = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_seat(self):
          return self.seat