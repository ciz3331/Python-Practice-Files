# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['bacon_lettuce_tomato', 'club', 'rueben', 'grilled cheese',\
                   'turkey','pastrami','ham and cheese', 'tuna salad', 'chicken salad',\
                    'veggie', 'pastrami','egg salad', 'pastrami', 'roast beef',\
                    'philly cheesesteak', 'italian submarine', 'meatball sub',\
                    'banh mi', 'pastrami', 'cuban', 'croissant',\
                    'peanut_butter_and_jelly', 'fish']
finished_sandwiches = []

print('The deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)