from django.db import models

# Create your models here.
class Utilities(models.Model):
    utility_type= models.CharField(max_length=50)
    date= models.DateField()
    amount= models.FloatField()

class GroceryDatesTotals(models.Model):
    purchase_date= models.DateField()
    tip= models.FloatField()
    grocery_total= models.FloatField()

class GroceryItemsBuyers(models.Model):
    purchase_date= models.DateField()
    item= models.CharField(max_length=50)
    quantity= models.FloatField()
    per_unit_price= models.FloatField()
    purchaser= models.CharField(max_length=50)

class GroceryPredictionFeatures(models.Model):
    item= models.CharField(max_length=50)
    asin= models.CharField(max_length=50)
    description= models.CharField(max_length=1000)
    purchaser= models.CharField(max_length=50)