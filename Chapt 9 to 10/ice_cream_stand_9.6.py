# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

from number_served import Restaurant

class IceCreamStand(Restaurant):
    """A class that inherits from class Restaurant"""
    def __init__(self,restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for temp_var in self.flavors:
            print(temp_var)


my_icecream_stand = IceCreamStand('ice cum', 'ice cream', 'strawberry',\
                                  'chocolate', 'vanilla')

my_icecream_stand.display_flavors()

