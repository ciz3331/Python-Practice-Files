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
