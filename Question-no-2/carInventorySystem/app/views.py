from django.shortcuts import render, redirect
from app.models import *
from app.forms import *

# Create your views here.
def addCarView(request):
  if request.method == 'POST':
    car_type = request.POST.get('car_type')
    name = request.POST.get('name')
    model = request.POST.get('model')
    year = request.POST.get('year')

    if car_type == 'electric':
      battery_capacity = request.POST.get('battery')
  
      ElectricCar.objects.create(
         name = name,
         model = model,
         year = year,
         battery_capacity = battery_capacity,
      )
    elif car_type == 'gas':
      fuel_efficiency = request.POST.get('fuel')
      GasCar.objects.create(
        name = name,
        model = model,
        year=year,
        fuel_efficiency = fuel_efficiency,
      )
    return redirect('car_list')
  return render(request, 'index.html')


def carDisplayView(request):
  electricCar = ElectricCar.objects.all()
  gasCar = GasCar.objects.all()
  
  context = {
    'electric_cars':electricCar,
    'gas_cars':gasCar,
  }
  return render(request, 'carShow.html', context)
