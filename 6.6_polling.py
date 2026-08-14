# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# •
#  Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •
# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_numbers = {
    'john smith' : '60',
    'emma johnson' : '36',
    'michael brown': '39',
    'sophia williams' : '05',
    'james jones' : '66',
}

#print(favorite_numbers)

favorite_numbers_poll = ['emily johnson', 'liam martinez', 'sophia brown',
                         'noah anderson', 'olivia garcia', 'james jones',
                         'jackson thompson', 'ava rodriguez', 'lucas davis',
                         'sophia williams', 'michael brown', 'mia wilson',
                         'ethan harris', 'emma johnson']

for poll in favorite_numbers_poll:
    if poll in favorite_numbers.keys():
        print(f"Hi {poll}, thank you for responding.")
    else:
        print(f"Hi {poll}, I would like to invite you to take the poll.")