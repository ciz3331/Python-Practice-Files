# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# •a.)
#  Use a conditional test in the while statement to stop the loop.
# •b.)
#  Use an active variable to control how long the loop runs.
# •c.)
#  Use a break statement to exit the loop when the user enters a 'quit' value.

#7.5 code
age = ""
while age != 'quit':
    age = input("Enter age, when done type 'quit' instead: ")
    price = 0
    
    if age != 'quit':
        age = int(age)

        if age < 3:
            price = 0
        elif age >= 3 and age <= 12:
            price = 10
        else:
            price = 15

        #print ticket price
        if price == 0:
            print("Your ticket is free.")
        else:
            print(f"Your ticket costs you ${price}")