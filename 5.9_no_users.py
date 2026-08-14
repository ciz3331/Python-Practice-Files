#5-9. No Users: Add an if test to hello_admin.py to make sure the list of 
#users is  not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct 
#message is printed.

usernames = ['jason_derulo', 'minami373', 'admin', 'atarayo', 'mrsuicidesheep']

#delete username elements:
for i in range(len(usernames)):
    #print(range(len(usernames)))
    #print(i)
    del usernames[-1]

print(usernames)

#check if list is empty:
if not usernames:
    print("We need to find some users!")
    

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status") 
        (" report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")


