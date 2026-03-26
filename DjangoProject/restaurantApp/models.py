from django.db import models

# Create your models here.

class OrderModel(models.Model):

    itemName = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.FloatField()
    orderTime = models.TimeField()
    orderStatus = models.CharField(max_length=50)

    def __str__(self):
        return self.itemName
