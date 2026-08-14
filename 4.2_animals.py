'''.
• 
• '''

# Animals: Think of at least three different animals that have a common 
# characteristic. Store the names of these animals in a list, and then use a for loop to 
# print out the name of each animal.
animals = ['dog', 'cat', 'hamster']
for animal in animals:
    print(animal)

print('')
# Modify your program to print a statement about each animal, such as A 
# dog would make a great pet.
for animal in animals:
    print("A " +animal +" would make a great pet.")

print('')
# Add a line at the end of your program, stating what these animals have in 
# common. You could print a sentence, such as Any of these animals would 
# make a great pet!
# i'm assuming it's inside the loop:

for animal in animals:
    print("A " +animal +" would make a great pet.")
    print("Any of these animals would make a great pet!")
