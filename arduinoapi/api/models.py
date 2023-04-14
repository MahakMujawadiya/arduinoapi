from django.db import models

# Create your models here.
class Config(models.Model):
    end_time=models.IntegerField(blank=True)
    start_time=models.IntegerField(blank=True)
    isOn=models.BooleanField(default=False)
    ssid=models.CharField(max_length=256,blank=True)
    password=models.CharField(max_length=256,blank=True)
    temp=models.FloatField(blank=True)