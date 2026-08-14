# # 8-16. Imports: Using a program you wrote that has one function in it, 
# store that function in a separate file. Import the function into your main 
# program file, and call the function using each of these approaches:


# import module_name
# import archived_messages
# old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# archived_messages.send_messages(old_list, new_list)
# archived_messages.show_messages(new_list)


# from module_name import function_name
from archived_messages import send_messages
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
send_messages(list1, list2)
#print(sent_msgs)
#show_messages(list2)


# from module_name import function_name as fn
# from archived_messages import send_messages as sm
# old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# sm(old_list, new_list)

# import module_name as mn
# import archived_messages as am
# old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []

# am.send_messages(old_list, new_list)

# from module_name import *
# from archived_messages import *
# old_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# send_messages(old_list, new_list)

#old_list comprehension version:
# old_list = [x for x in range(0,10)]
# print(old_list)