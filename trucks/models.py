from django.db import models
from truck_owner.models import Truck_Owner
# Create your models here.
class Trucks(models.Model):
    number_plate = models.CharField(max_length=45, primary_key=True)
    company_name = models.CharField(max_length=45)
    num_wheels = models.IntegerField()
    truck_owner = models.ForeignKey(Truck_Owner, on_delete=models.CASCADE) # truck_owner_id
