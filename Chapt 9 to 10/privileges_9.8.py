# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 
#9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

from login_attempts import User

class Privileges:
    """A class that will be an attribute for class Admin"""
    def __init__(self, privileges):
        self.privileges = privileges
    

    def show_privileges(self):
        print("List of privileges:")
        for temp_var in self.privileges:
            print(f"\t{temp_var.title()}")

class Admin(User):
    """A sub-class of User with special privileges"""

    def __init__(
            self, first_name, last_name, username, email, job, age, location,\
            privileges):
        super().__init__(first_name, last_name, username, email, job,\
                         age, location)
        self.privileges = Privileges(privileges)


privilege_list = ['can add post', 'can delete post', 'can ban user']
admin_sample = Admin('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
            'software engineer', 28, 'New York City',privilege_list)
admin_sample.privileges.show_privileges()
