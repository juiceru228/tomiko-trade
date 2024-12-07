from django.db import models

# Create your models here.
class Brand(models.Model):
    country = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    def __str__(self):
        return self.brand

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.IntegerField()
    transmission = models.CharField(max_length=50)
    engine_volume = models.CharField(max_length=50)
    drive = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    power_volume = models.CharField(max_length=50)
    brand_country = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.model} ({self.year})'
