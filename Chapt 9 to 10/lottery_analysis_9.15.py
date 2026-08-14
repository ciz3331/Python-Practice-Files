# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
# a loop that keeps pulling numbers until your ticket wins. Print a message report-
# ing how many times the loop had to run to give you a winning ticket.

import random
import string

#list containing numbers from 0 to 1 hundred
numbers = [x for x in range(0, 100)]
#randomly select 10 numbers from list numbers
ten_nums = [random.choice(numbers) for x in range(10)]

# Randomly choose a letter from a-z to A-Z 
five_letters = [random.choice(string.ascii_letters) for x in range(5)]
# print(ten_nums)
# print(five_letters)
lottery_list = ten_nums + five_letters
# print(lottery_list)

winner = tuple(random.sample(lottery_list,4))

# print(f"Any ticket matching these 4 numbers or letters wins a prize:\n\t{winner}")

#create a list of all number 0-99 and a-z and A-Z
def create_ticket_choices():
    ticket_choices = [x for x in range(0, 100)]
    letters = list(string.ascii_letters)

    while letters:
        temp = letters.pop()
        ticket_choices.append(temp)

    return tuple(ticket_choices)


def lottery_analysis(ticket_choices, winner):
    tries = 0
    while True:
        tries += 1
        current_ticket = generate_ticket(ticket_choices)
        if is_matching_ticket(current_ticket, winner):
            print(f"Total tries: {tries:,}")
            print(f"Current ticket: {current_ticket}")
            print(f"Winning ticket: {winner}")
            break
        
def generate_ticket(ticket_choices):        
    my_ticket = tuple(random.sample(ticket_choices,4))
    return my_ticket

def is_matching_ticket(ticket, winner):
    """Returns true only if our current ticket matches winner ticket, order
    does not matter"""
    digits_matched = 0

    for x in ticket:
        if x not in winner:
            break
        else:
            digits_matched += 1

    if digits_matched < 4:
        return False
    else:
        return True

lottery_analysis(create_ticket_choices(), winner)
print('Exit!')
