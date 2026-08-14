# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both meth-
# ods for each user.


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

    def describe_user(self):
        """Summarize user's attributes."""
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username.title()}")
        print(f"email: {self.email.title()}")
        print(f"job: {self.job.title()}")
        print(f"age: {self.age}")
        print(f"location: {self.location.title()}")

    def greet_user(self):
        "Greets user"
        print(f"Hello {self.first_name}, welcome to our program!")


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
