guest_list = ['Rachel Green', 'Monica Geller', 'Phoebe Buffay']

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

print(guest_list[1])
del guest_list[1]
guest_list.insert(1, 'Ross Geller')

for x in guest_list:
    print(f"Hello {x}, I would like to invite you to dinner!")

