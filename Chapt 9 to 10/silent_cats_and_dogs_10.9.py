# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-7 to fail
# silently if either file is missing.

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
    pass
    #print(e, type(e))
