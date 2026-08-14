class User:
    """A class of users with several attributes. Have a function to summarize
    those attributes and another function to greet the user."""

    def __init__(
            self, first_name, last_name, username, email, job, age, location):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.job = job
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Summarize user's attributes."""
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username.title()}")
        print(f"email: {self.email.title()}")
        print(f"job: {self.job.title()}")
        print(f"age: {self.age}")
        print(f"location: {self.location.title()}")

    def greet_user(self):
        """Greets user"""
        print(f"Hello {self.first_name}, welcome to our program!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attemprs to 0"""
        self.login_attempts = 0


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


# privilege_list = ['can add post', 'can delete post', 'can ban user']
# admin_sample = Admin('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
#             'software engineer', 28, 'New York City',privilege_list)
# admin_sample.privileges.show_privileges()