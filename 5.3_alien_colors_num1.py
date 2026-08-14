# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.


alien_color = 'Green'

# • Write an if statement to test whether the alien’s color is green. If it is, print 
# a message that the player just earned 5 points.
if alien_color.lower() == 'green':
    print("You just earned 5 points!")

# • Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)
#pass:
if alien_color.lower() == 'green':
    print("Awit yawa")
#fail:
if alien_color.lower() == 'yellow':
    print("Yawa E-N-A-O")