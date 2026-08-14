import math
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:


# • Print the message The last three items in the list are:. Then use a slice to 
# print the last three items in the list.

#i chose 4.8_cubes.py
cubes = []
for num in range(1,11):
    cubes.append(num**3)

for cube in cubes:
    print(cube)

print('')
print(f"cubes list is: {cubes}")


# • Print the message Three items from the middle of the list are:. Then use a 
#slice to print three items from the middle of the list.

print(f"The first three items in the list are: {cubes[:3]}")
print()

#i removed last item on cubes list so i can get the accurate 3 middle items:
# cubes.pop()
# print(f"cubes list is: {cubes}")

# • Print the message. Then use a 
# slice to print three items from the middle of the list.
#get the middle index which can be float
middle = len(cubes)/2
print(middle)
#round up the middle index and convert it to int
middle = math.ceil(middle)
print(middle)
middle = 4

print(f"Three items from the middle of the list are: "
    f"{cubes[middle-1 : middle+2]}")



