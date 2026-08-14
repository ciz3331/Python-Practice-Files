# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using json.dumps(), and read it back
# in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.

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

def greet_user():
    """Greet the user by username and prints other infos"""
    path = Path('user_info.json')

    if path.exists():
        print_user_info(get_stored_user_info(path))
    else:
        user_info = create_dict_user_info()
        store_dict_json(path, user_info)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()