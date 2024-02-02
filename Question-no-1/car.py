class Car:
  def __init__(self, name, model, year) -> None:
    self.name = name
    self.model = model
    self.year = year
  def show(self):
    print(f'''Car Information:
          {self.year} {self.name} {self.model}''')
    
class ElectricCar(Car):
  def __init__(self, name, model, year, battery_capacity) -> None:
    self.battery_capacity = battery_capacity
    super().__init__(name, model, year)
  
  def show(self):
    super().show()
    print(f"          Battery Capacity: {self.battery_capacity} kWh")
  

    

class GasCar(Car):
  def __init__(self, name, model, year, fuel_efficiency) -> None:
    self.fuel_efficiency = fuel_efficiency
    super().__init__(name, model, year)
  
  def show(self):
    super().show()
    print(f'          Fuel Efficiency: {self.fuel_efficiency} MPG')

   
def Car_Information():
  a = input("Enter car type (Electric/Gas): ")
 
  if a != 'Electric' and a != "Gas":
    print( "You are enter wrong car type. You can re-enter Electric/Gas type car.")
    return
  name = input("Enter Name: ")
  model = input("Enter model: ")
  year = input("Enter Year: ")
  
  if a == 'Electric':   
    battery = input("Enter battery capacity (kWh): ")
    eletric_car = ElectricCar(name, model, year, battery)
    eletric_car.show()
  elif a == 'Gas':   
    battery = input("Enter fuel efficiency (MPG): ")
    gas_car = GasCar(name, model, year, battery)
    gas_car.show()
    
### Electric Car Information
Car_Information()
### Gas Car Information
Car_Information()


    