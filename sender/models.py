from django.db import models
from truck_owner.models import Truck_Owner
# Create your models here.

class Sender(models.Model):
    sender_id = models.CharField(max_length=45,  primary_key=True)
    order_id = models.CharField(max_length=45)
    truck_owner = models.ForeignKey(Truck_Owner, on_delete=models.CASCADE)