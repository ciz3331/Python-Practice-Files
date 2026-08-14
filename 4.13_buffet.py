# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
simple_foods = ('pizza', 'pasta', 'salad bar', 'fried chicken', 'soup and bread')

# • Use a for loop to print each food the restaurant offers.
for simple_food in simple_foods:
    print(simple_food)

# • Try to modify one of the items, and make sure that Python rejects the 
# change.
#code with error:
# simple_foods[0] = 'pussy meat'

print('')    
# • The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.
simple_foods = ('pizza', 'pasta', 'salad bar', 'stir-fry station',\
                 'indian curry')
for simple_food in simple_foods:
    print(simple_food)





