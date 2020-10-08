from django.db import models

# Create your models here.

class Posts(models.Model):
    CHOICES = (
        ("corporate", 'corporate'),
        ("sports", 'sports'),
        ("weddings", 'weddings'),
        ("documentaries",'documentaries')
    )
    images = models.ImageField(upload_to = 'uploads/')
    category = models.CharField(choices = CHOICES , max_length = 50)

class Clients(models.Model):
    logos = models.ImageField(upload_to= 'uploads')