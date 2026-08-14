# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

from pathlib import Path
import json


def get_fav_num():
    try:
        fav_num = int(input("Enter your favorite number: "))
        return fav_num
    except ValueError as e:
        print(e, type(e))

path = Path('favorite_number2.json')
if path.exists():   
    print(f"I know your favorite number! It's {json.loads(path.read_text())}")
else:
    path.write_text(json.dumps(get_fav_num()))