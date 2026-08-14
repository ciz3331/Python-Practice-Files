# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#from 5.4:
alien_color = 'yellow'
if alien_color == 'red':
    print("Alien color is red")
else:
    print("Alien color is not red")
#convert if-else to if-elif-else
if alien_color == 'red':
    print("Alien color is red")
elif alien_color == 'green':
    print("Alien color is green")
else:
    print("Alien color is yellow")

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed 
# for the appropriate color alien
#version 1: RGY
if alien_color == 'red':
    print("You just earned 15 points!")
elif alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
#version 2: YRG
if alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 5 points!")
#version 3: GYR:
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")