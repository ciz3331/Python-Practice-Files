# 10-14. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who last
# used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.

from pathlib import Path
import json

def get_username():
    """Prompt for a new username."""
    username = input("What is your username? ")
    return username

def get_user_age():
    """Prompt user for age"""
    try:
        age = int(input("Enter your age: "))
    except ValueError as e:
        print(e, type(e))
        return None
    else:
        return age

def get_user_gender():
    """Prompt user for gender"""
    gender = input("Enter your gender: ")
    return gender

def get_user_full_name():
    """Prompt user for full name"""
    full_name = input("Enter your full name: ")
    return full_name

def create_dict_user_info():
    """Creates and returns User info dictionary"""
    user_info = {
                    'username' : get_username(),
                    'full name' : get_user_full_name(),
                    'age' : get_user_age(),
                    'gender' : get_user_gender(),
                }
    return user_info

def store_dict_json(path, user_info):
    """Stores the user_info dictionary to a .json file"""
    path.write_text(json.dumps(user_info))

def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        user_info = json.loads(path.read_text())
        return user_info
    else:
        return None
    
def print_user_info(user_info):
    """Prints a dictionary"""
    print(f"Hello, {user_info['username']}...below are your other user"
          f" information:")

    for k, v in user_info.items():
        if k != 'username':
            print(f"\tYour {k} is {v}")

def verify_user(user_info):
    while True:
        answer = input(f"Is this your username? y/n: {user_info['username']}: ")
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Please enter 'y' or 'n' only!")
            continue

def else_greet_user(path, user_info):
    user_info = create_dict_user_info()
    store_dict_json(path, user_info)
    print(f"We'll remember you when you come back, "
            f"{user_info['username']}!")
    
def greet_user():
    """Greet the user by username and prints other infos"""
    path = Path('user_info.json')

    if path.exists():
        user_info = get_stored_user_info(path)
        if verify_user(user_info):
            print_user_info(user_info)
        else:
            else_greet_user(path, user_info)
    else:
        else_greet_user(path, user_info)
    
greet_user()