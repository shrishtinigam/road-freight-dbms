from django.shortcuts import render
from .models import Sender
from transaction.models import Transaction
from truck_owner.models import Truck_Owner
from trucks.models import Trucks
# Create your views here.

def sender_detail_view(request, sender_id):
    sender_obj = Sender.objects.get(sender=sender_id)
    #truck_owner_obj = Truck_Owner.objects.get()
    #transaction_obj = None
    #transaction_obj = Transaction.objects.get(transaction=)
    