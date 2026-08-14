#mmddyy
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

bday = input('Enter your birthday(format: mmddyy):')

if bday in contents:
    bday_index = (contents.index(bday)) - 2
    print(f"Your birthday {bday} is on Pi! It's on decimal place:"
          f"{bday_index}")
else:
    print("Sorry! Your birthday is not on Pi!")