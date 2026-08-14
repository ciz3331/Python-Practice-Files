# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program, or improving the formatting of the output.

#from last example for chapter 6 -> many_users.py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'favorite foods' : ['spaghetti carbonara', 'sushi', 'chocolate cake'],
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'favorite foods' : ['croissant', 'vegetable pad thai', 'cheesecake'],
    },
}

for username, user_info in users.items():

    print(f"\nUsername: {username}")
    print(f"testingcj: {user_info}")

    full_name = f"{user_info['first']} {user_info['last']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {user_info['location'].title()}")

    #favorite foods
    print("\tFavorite foods: ")
    for favorite_food in user_info['favorite foods']:
        print(f"\t\t{favorite_food}")