from Car import Car



class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")





class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


    def upgrade_battery(self):
        """Upgrade the battery size to 100 kWh if it's not already."""
        if self.battery_size != 100:
            self.battery_size = 100

my_electric_car = ElectricCar("Tesla", "Model S", 2023)
my_electric_car.battery.describe_battery()  
