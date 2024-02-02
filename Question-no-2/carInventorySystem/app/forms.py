from app.models import *
from django import forms
class carForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

class electricCarForm(forms.ModelForm):
  class Meta:
    model = ElectricCar
    fields = '__all__'

class gasCarForm(forms.ModelForm):
  class Meta:
    model = GasCar
    fields = '__all__'

