'''4-1. Pizzas: 
• 
• '''

#Think of at least three kinds of your favorite pizza. Store these 
#pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['pepperoni', 'margherita', 'hawaiian']

for pizza in pizzas:
    print(pizza)

#Modify your for loop to print a sentence using the name of the pizza, 
#instead of printing just the name of the pizza. For each pizza, you should 
#have one line of output containing a simple statement like I like pepperoni pizza.

for pizza in pizzas:
    print("I like " +pizza +" pizza")

#Add a line at the end of your program, outside the for loop, that states 
#how much you like pizza. The output should consist of three or more lines 
#about the kinds of pizza you like and then an additional sentence, such as 
#I really love pizza!


for pizza in pizzas:
    print("I like " +pizza +" pizza")
    
#below is outside the loop
print("Pizza is undeniably one of the most beloved foods globally, with its\n"
"irresistible combination of gooey cheese, flavorful sauce, and endless topping\n"
"possibilities. Its versatility allows it to cater to a wide range of tastes,\n"
"whether you prefer classic pepperoni or adventurous combinations like BBQ\n"
"chicken or spinach and feta. The joy of sinking your teeth into a hot,\n"
"fresh slice is unparalleled, making pizza a timeless favorite for gatherings,\n"
"solo indulgences, and everything in between.")
print("I really love pizza!")


