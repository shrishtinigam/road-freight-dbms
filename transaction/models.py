from django.db import models
from trucks.models import Trucks
from receiver.models import Receiver
# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=45,  primary_key=True)
    wt_ore = models.FloatField()
    type_ore = models.CharField(max_length=45)
    from_dest = models.CharField(max_length=45)
    to_dest = models.CharField(max_length=45)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    fastag = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    number_plate = models.ForeignKey(Trucks, on_delete=models.CASCADE) #FOREIGN KEYS
    receiver_id = models.ForeignKey(Receiver, on_delete=models.CASCADE) #FOREIGN KEYS 

