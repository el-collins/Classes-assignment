

from classes.Restuarant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = ['vanilla', 'chocolate', 'strawberry', 'mint']

    def display_flavour(self):
        print("Available flavour:")
        for flavor in self.flavour:
            print(flavor)

# Exercise 9-6
ice_cream_stand = IceCreamStand("Cold stone", "Ice Cream")
ice_cream_stand.display_flavour()