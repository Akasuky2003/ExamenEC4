from django.db import models
from django.db.models.fields import CharField,URLField,DateTimeField
from django.db.models.fields.files import ImageField
from django.utils import timezone

class Services(models.Model):
    title= CharField(max_length=100)
    description= CharField(max_length=250)
    image= ImageField(upload_to='blog/images')
    url= URLField(blank=True)
    timestamp = DateTimeField(default=timezone.now)