# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

dream_vacation_poll = { }
poll_active = True

while poll_active:
    name = input("Enter name\n(If you desire to quit, type 'quit': ")
    
    if name == 'quit':
        poll_active = False
    else:
        place = input('If you could visit one place in the world, where would you go? ')
        dream_vacation_poll[name] = place

#print poll results:
print("Here are the poll results: ")

for name, place in dream_vacation_poll.items():
    print(f"\t{name.title()} wants to go to {place.title()}")