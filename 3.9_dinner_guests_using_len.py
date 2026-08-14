#3.4:
guest_list = ['Rachel Green', 'Monica Geller', 'Phoebe Buffay']

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

len_3_point_4 = len(guest_list)

#3.5:
guest_list = ['Rachel Green', 'Monica Geller', 'Phoebe Buffay']

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(guest_list[1])
del guest_list[1]
guest_list.insert(1, 'Ross Geller')

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

len_3_point_5 = len(guest_list)

#3.6:
guest_list = ['Rachel Green', 'Monica Geller', 'Phoebe Buffay']

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(guest_list[1])
del guest_list[1]
guest_list.insert(1, 'Ross Geller')

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(f"Current guest list: {guest_list}")

guest_list.insert(0, 'Joey Tribbiani')
#print(guest_list)

guest_list_middle_slot = int(((len(guest_list))/2))
guest_list.insert(guest_list_middle_slot, 'Chandler Bing')

guest_list.append('Mike Hannigan')

print("\nNew invitations:")
for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

len_3_point_6 = len(guest_list)

#3.7:
guest_list = ['Rachel Green', 'Monica Geller', 'Phoebe Buffay']

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(guest_list[1])
del guest_list[1]
guest_list.insert(1, 'Ross Geller')

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(f"Current guest list: {guest_list}")

guest_list.insert(0, 'Joey Tribbiani')
#print(guest_list)

guest_list_middle_slot = int(((len(guest_list))/2))
guest_list.insert(guest_list_middle_slot, 'Chandler Bing')

guest_list.append('Mike Hannigan')

print("\nNew invitations:")
for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

#start of exercise 3.7
print("\nStart of exercise 3.7\n")
for x in guest_list:
    print(f"Hello {x}, I can now only invite 2 people for the dinner")
print(f"\ncurrent guest: {guest_list}")

print("\nSorry cancel invitation letters: \n")
while(len(guest_list) > 2):
    print(f"Sorry, {guest_list.pop()} I would like to cancel my dinner"
          f"invitation to you") 
print(f"\ncurrent guest: {guest_list}")

for x in guest_list:
    print(f"Hi, {x}, you are still invited for the dinner")

while((len(guest_list)) > 0):
    del guest_list[0]

print(guest_list)

len_3_point_7 = len(guest_list)
print(len_3_point_7)

#3.9 exercise:
print("lengths compiled:")
def len_exercises():
    len_compiled = [len_3_point_4, len_3_point_5, len_3_point_6, len_3_point_7]
    for x in len_compiled:
        print(f"guest_list: {x}")

len_exercises()




