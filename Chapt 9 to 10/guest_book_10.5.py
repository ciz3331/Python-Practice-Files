# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect
# all the names that are entered, and then write these names to a file called
# guest_book.txt. Make sure each entry appears on a new line in the file.

from pathlib import Path

guest_book_str = ''

while True:
    name = input("Type 'q' to quit!\nEnter your name: ")
    if name == 'q':
        break
    else:
        guest_book_str += (f"{name}\n")

path = Path('guest_book.txt')
path.write_text(guest_book_str.strip())