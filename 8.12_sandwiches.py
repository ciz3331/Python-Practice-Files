# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

#added 2 parameters to test function behavior
def make_sandwich(name,age=None,*items):
    """Accepts a list of items that a person wants on a sandwich"""
    print(f"Hello {name.title()}, i've made your sandwich with the following ingredients: ")
    print(f"age: {age}")
    for item in items:
        print(f"\t{item.title()}")


#person 1
make_sandwich('alice',69,'turkey', 'lettuce', 'tomato', 'swiss cheese', 'mustard',\
              'bacon', 'avocado')

#person 2
make_sandwich('bob', 'ham', 'cheddar cheese', 'pickles', 'mayonnaise', 'lettuce',\
              'tomato', 'onion', 'jalapenos')

#person 3
make_sandwich('charlie','roast beef', 'provolone cheese', 'red onion', 'avocado',\
              'chipotle sauce', 'bacon', 'spinach', 'cucumber', 'sriracha')