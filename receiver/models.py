from django.db import models

# Create your models here.


class Receiver(models.Model):
    receiver_id = models.CharField(max_length=45,  primary_key=True)
    fastag = models.CharField(max_length=45)
    date = models.DateField()
    timestamp = models.TimeField()

    class Meta:
        unique_together = (('receiver_id', 'fastag'),) 

