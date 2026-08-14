# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

from login_attempts import User

class Admin(User):
    """A sub-class of User with special privileges"""

    def __init__(
            self, first_name, last_name, username, email, job, age, location,
            privileges):
        super().__init__(first_name, last_name, username, email, job,\
                         age, location)
        self.privileges = privileges

    def show_privileges(self):
        print("List of privileges:")
        for temp_var in self.privileges:
            print(f"\t{temp_var.title()}")

privilege_list = ['can add post', 'can delete post', 'can ban user']
admin_sample = Admin('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
            'software engineer', 28, 'New York City',privilege_list)
admin_sample.show_privileges()