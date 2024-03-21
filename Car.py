# class Human:
#     def __init__(self, country, gender) -> None:
#         self.country = country
#         self.gender = gender
#         self.age = 0
#         if self.country == "nigeria":
#             self.age = 20
#     def sleep(self):
#         return f"Go to sleep young {self.gender}"


# clara = Human("Nigeria", "Female")
# print(clara.country)
# print(clara.sleep())

# david = Human("Nigeria", "Male")
# print(david.gender)
# david.gender = "Female"
# print(david.gender)

# ikem = Human("nigeria","Male")
# print(ikem.age)

# kosi = Human("Japan","Male")
# print(kosi.age)


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.moving = False
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage:int):
        if mileage > self.odometer_reading: 
            self.odometer_reading = mileage

    def increase_odometer(self, miles:float):
        self.odometer_reading += miles
    
    def drive_car(self):
        self.moving = True

    def date_difference(self, current_year: int):
        """Takes a year and calculates the total of year the car is"""
        if current_year > self.year:
            difference = current_year - self.year
            return difference  
        else:   
            return "The car was made after this year!"
       
        



