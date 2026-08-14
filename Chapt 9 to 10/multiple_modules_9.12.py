from user import User
from privileges_admin import Privileges, Admin

privilege_list = ['can add post', 'can delete post', 'can ban user']
admin_sample = Admin('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
            'software engineer', 28, 'New York City',privilege_list)
admin_sample.privileges.show_privileges()