# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each instance.

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

restaurant1 = Restaurant('resto_fish', 'seafoods')
restaurant2 = Restaurant('resto_pork', 'baboy')
restaurant3 = Restaurant('resto_beef', 'baka')

#calling describe_restaurant() for each instances
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()