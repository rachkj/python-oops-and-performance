class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Electric:
    def __init__(self, battery):
        self.battery = battery

    def info(self):
        return f"Battery: {self.battery} kWh"

class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, battery):
        super().__init__(brand)
        Electric.__init__(self, battery)

    def info(self):
        vehicle_info = super().info()
        electric_info = Electric.info(self)
        return f"{vehicle_info}, {electric_info}"

car = ElectricCar("Tesla", 75)
print(car.info())
