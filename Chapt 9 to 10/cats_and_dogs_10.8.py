# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file.
#  Write a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.

from pathlib import Path

cats = Path('cats.txt')
dogs = Path('dogs.txt')

def print_names(list_names):
    """print list elemenets in tabbed manner"""
    for list_name in list_names:
        print(f"\t{list_name}")

try:
    str_cats = cats.read_text().splitlines()
    str_dogs = dogs.read_text().splitlines()
    print(f"Cat names:")
    print_names(str_cats)
    print(f"Dog names:")
    print_names(str_dogs)
except FileNotFoundError as e:
    print(e, type(e))

