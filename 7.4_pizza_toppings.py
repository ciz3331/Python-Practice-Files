# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

msg_toppings = "Enter a topping to add"
msg_toppings += "\nWhen you're done, type 'quit' instead: "

toppings = ""
while toppings != 'quit':
    toppings = input(msg_toppings)
    if toppings != 'quit':
        print(f"\nAdding {toppings} to your pizza...\n")