# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

whiskers = {
    'pet name' : 'whiskers',
    'kind of animal' : 'cat',
    "owner's name" : 'sarah',
}

rocky = {
    'pet name' : 'rocky',
    'kind_of_animal' : 'dog',
    "owner's name" : 'mike',
}

luna = {
    'pet name' : 'luna',
    'kind_of_animal' : 'rabbit',
    "owner's name" : 'emily',
}

gizmo = {
    'pet name' : 'gizmo',
    'kind_of_animal' : 'hamster',
    "owner's name" : 'alex',
}

oliver = {
    'pet name' : 'oliver',
    'kind_of_animal' : 'bird',
    "owner's name" : 'jessica',
}


pets = [whiskers, rocky, luna, gizmo, oliver]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} is {value}")
    print()