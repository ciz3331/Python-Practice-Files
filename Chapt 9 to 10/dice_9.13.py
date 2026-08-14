# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a random num-
# ber between 1 and the number of sides the die has. Make a 6-sided die and
# roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import random

class Die:
    """A simple die simulation with 1 attribute called sides"""
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        list_sides = list(range(1,self.sides+1))
        # print(list_sides)
        return random.choice(list_sides)


my_die = Die()
my_die_10_sides = Die(10)
my_die_20_sides = Die(20)

def print_10_times(die_obj):
    for x in range(10):
        print(die_obj.roll_die())

print("Printing 6 sides die 10 times")
print_10_times(my_die)

print("Printing 10 sides die 10 times")
print_10_times(my_die_10_sides)

print("Printing 20 sided die 10 times")
print_10_times(my_die_20_sides)