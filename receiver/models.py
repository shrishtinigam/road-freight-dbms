from django.db import models

# Create your models here.
class Receiver(models.Model):
    fastag = models.CharField(max_length=45, primary_key=True)
    receiver = models.CharField(max_length=45) # receiver_id
    date = models.DateField(null=True, blank=True)
    timestamp = models.TimeField(null=True, blank=True)