# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 
# 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
list_one2nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# • Loop through the list.
# for one2nine in list_one2nine:
#     if one2nine == 1:
#         print(f"{one2nine}st")
#     elif one2nine == 2:
#         print(f"{one2nine}nd")
#     elif one2nine == 3:
#         print(f"{one2nine}rd")
#     else:
#         print(f"{one2nine}th")
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending 
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 
# 8th 9th", and each result should be on a separate line
        
#efficient version:
for one2nine in list_one2nine:
    if one2nine > 3:
        print(f"{one2nine}th")
    elif one2nine == 1:
        print(f"{one2nine}st")
    elif one2nine == 2:
        print(f"{one2nine}nd")
    elif one2nine == 3:
        print(f"{one2nine}rd")