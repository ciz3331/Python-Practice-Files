# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store
# the classes User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that everything is
# working correctly.

#from user_privileges_admin import User, Privileges, Admin
import user_privileges_admin

privilege_list = ['can add post', 'can delete post', 'can ban user']
admin_sample = user_privileges_admin.Admin('John', 'Smith', 'jsmith123', 'jsmith123@example.com',\
            'software engineer', 28, 'New York City',privilege_list)
admin_sample.privileges.show_privileges()

