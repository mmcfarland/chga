from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
  
class Farmer(models.Model):
    farm = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address)
    
class Buyer(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address)
    
class SupplyList(models.Model):
    farmer = models.ForeignKey(Farmer)
    created_date = models.DateTimeField('date created')
    pickup_date = models.DateField('date to be picked up')

class ItemInfo(models.Model):
    quantity = models.IntegerField()
    units = models.CharField(max_length=10)
    item = models.CharField(max_length=100)
    variety = models.CharField(max_length=200)
    can_truck = models.BooleanField()

    class Meta:
        abstract=True
    
class SupplyItem(ItemInfo):
    supply_list = models.ForeignKey(SupplyList)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    can_barter = models.BooleanField()

class BarterItem(ItemInfo):
    pickup_date = models.DateField('date barter item is to be picked up')    

class SaleInfo(models.Model):
    supply_item = models.ForeignKey(SupplyItem)
    quantity = models.IntegerField()
    truck = models.BooleanField()
    truck_dropoff = models.ForeignKey(Address, related_name='+', null=True)
    truck_dropoff_note = models.TextField(null=True)
    truck_pickup = models.ForeignKey(Address, related_name='+', null=True)
    truck_pickup_note = models.TextField(null=True)
    
    class Meta:
        abstract=True

class Sale(SaleInfo):
    buyer = models.ForeignKey(Buyer)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Barter(SaleInfo):
    farmer = models.ForeignKey(Farmer)
    barter_item = models.ForeignKey(BarterItem)
    barter_pickup = models.ForeignKey(Address, related_name='+', null=True)
    barter_pickup_note = models.TextField(null=True)   
    barter_dropoff = models.ForeignKey(Address, related_name='+', null=True)
    barter_dropoff_note = models.TextField(null=True)
 
