# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

person_1 = {
    'first name' : 'John',
    'last name' : 'Smith',
    'age' : 69,
    'city' : 'New York',
}

person_2 = {
    'first name' : 'Charlotte',
    'last name' : 'Lee',
    'age' : 34,
    'city' : 'Seattle',
}

person_3 = {
    'first name' : 'Benjamin',
    'last name' : 'Nguyen',
    'age' : 27,
    'city' : 'Toronto',
}

people = [person_1,person_2,person_3]

for person in people:
    for key, value in person.items():
        if key != 'city':
            print(f"{key} is {value}")
        else:
            print(f"from {value} {key}")
    print()   