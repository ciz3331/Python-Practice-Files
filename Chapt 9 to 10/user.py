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