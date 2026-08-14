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
            self, first_name, last_name, username, email, job, age, location,):
        
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


user1 = User('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
            'software engineer', 28, 'New York City')

user2 = User('Lisa', 'Johnson', 'ljohnson456', 'ljohnson456@example.com',\
            'marketing manager', '35', 'los angeles')

user3 = User('Raj', 'Kumar', 'rkumar789', 'rkumar789@example.com',\
            'data analyst', 32, 'bangalore')

#calling both methods in class User for all users
print("User1:")
user1.describe_user()
user1.greet_user()

print("\nUser2:")
user2.describe_user()
user2.greet_user()

print("\nUser3:")
user3.describe_user()
user2.greet_user()

#Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
#We'll use user1 for this
print("\nexercise 9.5 continuation:\n")
for temp_var in range(10):
    user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts: {user1.login_attempts}")

