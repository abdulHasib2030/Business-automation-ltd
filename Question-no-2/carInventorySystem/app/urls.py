from django.urls import path
from app.views import *

urlpatterns = [
  path('', addCarView, name='add_car'),    
  path('show/', carDisplayView, name='car_list')
]
