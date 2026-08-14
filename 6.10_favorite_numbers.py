# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {
    'john smith' : [60, 12, 45, 78],
    'emma johnson' : [36, 34, 56, 91],
    'michael brown': [39, 22, 67, 11],
    'sophia williams' : [5, 89, 33, 55],
    'james jones' : [66, 7, 82, 19],
}

for name, fav_num in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for one_fav_num in fav_num:
        print(one_fav_num)
    print()