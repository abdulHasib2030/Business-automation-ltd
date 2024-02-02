from django.db import models

# Create your models here.
class Car(models.Model):
  name = models.CharField(max_length = 200)
  model = models.CharField(max_length = 200)
  year = models.IntegerField()

class ElectricCar(Car):
  battery_capacity = models.DecimalField(max_digits=5, decimal_places = 2)

class GasCar(Car):
  fuel_efficiency = models.DecimalField(max_digits=5, decimal_places = 2)