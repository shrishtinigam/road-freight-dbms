from django.db import models

# Create your models here.
class Truck_Owner(models.Model):
    truck_owner = models.CharField(max_length=45,  primary_key=True) # truck_owner_id
    truck_owner_name = models.CharField(max_length=45)
    num_trucks = models.CharField(max_length=45)
 

