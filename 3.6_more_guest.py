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
