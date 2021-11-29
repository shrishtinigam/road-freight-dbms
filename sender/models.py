from django.db import models

# Create your models here.

class Sender(models.Model):
    sender_id = models.CharField(max_length=45,  primary_key=True)
    order_id = models.CharField(max_length=45)