from django.db import models
from sender.models import Sender
# Create your models here.

class Driver(models.Model):
    driver = models.CharField(max_length=45,  primary_key=True) # driver_id
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE) # sender_id
    
