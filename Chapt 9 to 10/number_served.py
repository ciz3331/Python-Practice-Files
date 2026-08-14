"""A copy of number_served_9.4.py to be used for import"""

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.


class Restaurant:
    """A simple restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Below are my attributes:")
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is now open")
    
    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served


restaurant = Restaurant('arigatou', 'japanese seafoods')
print(f"Printing self.restaurant_name: {restaurant.restaurant_name}")
print(f"Printing self.cuisine_type: {restaurant.cuisine_type}")
print(f"customers served: {restaurant.number_served}")
restaurant.number_served = 69
print(f"\n via Attribute:\tcustomers served: {restaurant.number_served}")
restaurant.set_number_served(16)
print(f"\n via method: \tcustomers served: {restaurant.number_served}")
restaurant.increment_number_served(50)
print(f"\n via method increment: \tcustomers served: {restaurant.number_served}")

