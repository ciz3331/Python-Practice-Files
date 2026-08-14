# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message “I know your favorite
# number! It’s _____.”
from pathlib import Path
import json
try:
    fav_num = int(input("Enter your favorite number: "))
    Path('favorite_number.json').write_text(json.dumps(fav_num))
except ValueError as e:
    print(e, type(e))