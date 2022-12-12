from django.db import models
import datetime

class Services(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    image= models.ImageField(upload_to='index/images')
    url= models.URLField(blank=True)
    timestamp = models.DateTimeField(datetime.datetime.today)