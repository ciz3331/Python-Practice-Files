'''
3-8. Seeing the World: Think of at least five places in the world you’d like 
to visit.
    
    

    Great Wonders of the world:
1. The Great Wall of China
2. Chichen Itza
3. Petra 
4. Machu Picchu
5. Christ the Redeemer
6. The Colosseum
7. Taj Mahal
8. Angkor Wat
'''
#Store the locations in a list. Make sure the list is not in alphabetical order.
world_wonders = ['the great wall of china', 'chichen itza', 'petra', \
                'machu picchu', 'christ the redeemer', 'the colosseum',\
                'taj mahal', 'angkor wat']

#Print your list in its original order. Don’t worry about printing the 
#list neatly; just print it as a raw Python list.
print("Original:")
print(world_wonders)

#Use sorted() to print your list in alphabetical order without modifying the 
#actual list.
print("\n Alphabetical sort temp:")
print(sorted(world_wonders))

#Show that your list is still in its original order by printing it.
print("\nOriginal again:")
print(world_wonders)

#Use sorted() to print your list in reverse-alphabetical order without 
#changing the order of the original list.
print("\n reversed alphabetical order:")
print(sorted(world_wonders,reverse=True))

#• Show that your list is still in its original order by printing it again.
print("\nOriginal again:")
print(world_wonders)

#• Use reverse() to change the order of your list. Print the list to show that its 
#    order has changed.
print("\n reversed the list:")
world_wonders.reverse()
print(world_wonders)

#• Use reverse() to change the order of your list again. Print the list to show 
#    it’s back to its original order.
world_wonders.reverse()
print("\nOriginal again:")
print(world_wonders)

#• Use sort() to change your list so it’s stored in alphabetical order. Print the 
#    list to show that its order has been changed.
print("\n Permanent alphabetical order:")
world_wonders.sort()
print(world_wonders)

#• Use sort() to change your list so it’s stored in reverse-alphabetical order. 
#    Print the list to show that its order has changed.
print("\n Permanent reverse alphabetical order:")
world_wonders.sort(reverse=True)
print(world_wonders)