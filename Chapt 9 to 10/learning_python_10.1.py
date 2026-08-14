# 10-1. Learning Python: Open a blank file in your text editor and write a few lines
# summarizing what you’ve learned about Python so far. Start each line with the
# phrase In Python you can. . . . Save the file as learning_python.txt in the same
# directory as your exercises from this chapter. Write a program that reads the file
# and prints what you wrote two times: print the contents once by reading in the
# entire file, and once by storing the lines in a list and then looping over each line.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

#print the contents once by reading in the entire file
print('print the contents once by reading in the entire file:')
print(contents)

#once by storing the lines in a list and then looping over each line.
print('once by storing the lines in a list and then looping over each line:')
contentlines = path.read_text().splitlines()
for contentline in contentlines:
    print(contentline)