class Restaurant:
    """A simple restaurant class with methods to manage the state of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant with a name and cuisine type.

        :param restaurant_name: The name of the restaurant.
        :type restaurant_name: str
        :param cuisine_type: The type of cuisine served at the restaurant.
        :type cuisine_type: str
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Initialize the number of customers served.

    def describe_restaurant(self):
        """Print the name and cuisine type of the restaurant.

        This method is useful for providing a quick overview of the restaurant.
        """
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number: int):
        """Set the number of customers served.

        :param number: The new number of customers served.
        :type number: int
        """
        self.number_served = number

    def increment_number_served(self, number: int):
        """Increment the number of customers served.

        :param number: The number of customers to add to the current count.
        :type number: int
        """
        self.number_served += number


# Create an instance of the Restaurant class
restaurant = Restaurant("Delicious Bites", "Italian")

# Print the initial number of customers served
print(f"Customer served: {restaurant.number_served}")

# Set the number of customers served to 13
restaurant.number_served = 13
print(f"Customer served: {restaurant.number_served}")

# Set the number of customers served to 15
restaurant.set_number_served(15)
print(f"Customer served: {restaurant.number_served}")

# Increment the number of customers served by 7
restaurant.increment_number_served(7)
print(f"Customer served: {restaurant.number_served}")


