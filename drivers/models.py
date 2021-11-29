from django.db import models

# Create your models here.

class Driver(models.Model):
    sender_id = models.CharField(max_length=45,  primary_key=True)
    driver_id = models.CharField(max_length=45)

    class Meta:
        unique_together = (('sender_id', 'driver_id'),) 