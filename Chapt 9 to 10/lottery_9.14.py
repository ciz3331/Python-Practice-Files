# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 
# letters.Randomly select 4 numbers or letters from the list and print a message 
# saying that any ticket matching these 4 numbers or letters wins a prize.

import random
import string

#list containing numbers from 0 to 1 Million
numbers = [x for x in range(0, 1_000_001)]
#randomly select 10 numbers from list numbers
ten_nums = [random.choice(numbers) for x in range(10)]

# Randomly choose a letter from a-z to A-Z 
five_letters = [random.choice(string.ascii_letters) for x in range(5)]

print(ten_nums)
print(five_letters)

lottery_list = ten_nums + five_letters
print(lottery_list)

winner = [random.choice(lottery_list) for x in range(4)]
print(f"Any ticket matching these 4 numbers or letters wins a prize:\n\t{winner}")
