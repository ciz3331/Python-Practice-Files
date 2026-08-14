"""A copy of login_attempts_9.5.py to use for import"""

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

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



