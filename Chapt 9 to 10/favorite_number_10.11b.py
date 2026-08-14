# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message “I know your favorite
# number! It’s _____.”
from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():   
    print(f"I know your favorite number! It's {json.loads(path.read_text())}")
else:
    print('file named favorite_number.txt does not exist!')