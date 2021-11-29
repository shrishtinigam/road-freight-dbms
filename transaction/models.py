from django.db import models
from trucks.models import Trucks
from receiver.models import Receiver
# Create your models here.

class Transaction(models.Model):
    transaction = models.CharField(max_length=45,  primary_key=True) # transaction_id
    wt_ore = models.FloatField()
    type_ore = models.CharField(max_length=45)
    from_dest = models.CharField(max_length=45)
    to_dest = models.CharField(max_length=45)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    fastag = models.ForeignKey(Receiver, on_delete=models.CASCADE) #FOREIGN KEYS
    status = models.CharField(max_length=45)
    number_plate = models.ForeignKey(Trucks, on_delete=models.CASCADE) #FOREIGN KEYS

