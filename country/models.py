from django.db import models

# Create your models here.
class country(models.Model):

    countryName = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    countryImage = models.ImageField(default='default.jpg',upload_to='countryImage/')
    nativeName =models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    population = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.countryName