# for list1_element in list1:
#   if list1_element in list2:

# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
current_users = ["john_Doe", "Alice123", "coding_cat", "pythonista",\
                 "webdev_guru"]
# • Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
new_users = ["data_scientist", "alice123", "design_wizard", "security_expert",\
             "pythonista"]
# • Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.)

#what happened here is we defined a new list named "current_users", which
#effectively de-referenced the old version of "current_users". Then we appended
#all elements of the old version of "current_users" in lowercase to the new list.
#copy list to lowercase:
current_users = [current_user.lower() for current_user in current_users]
print(current_users)

for current_user in current_users:
    if current_user in new_users:
        print(f"The username {current_user} has already been used.")
        new_users.remove(current_user)
        replace_username = input("Enter the new username: ")
        new_users.append(replace_username.lower())

print(f"new_users: {new_users}")



