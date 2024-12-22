from django.db import models

# Create your models here.
class bids(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
   
    class Meta:
        db_table = 'bids'
