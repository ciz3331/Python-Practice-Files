# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open. Make an instance called restaurant from 
# your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    """A simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Below are my attributes:")
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is now open")


restaurant = Restaurant('arigatou', 'japanese seafoods')
print(f"Printing self.restaurant_name: {restaurant.restaurant_name}")
print(f"Printing self.cuisine_type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()