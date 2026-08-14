# 10-2. Learning C: You can use the replace() method to replace any word in a 
# string with a different word. Here’s a quick example showing how to replace 
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, 
# and replace the word Python with the name of another language, such as C. 
# Print each modified line to the screen.
#I got no word python, so let's change 'chapter' to 'pagsubok' instead.
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

contents = contents.replace('chapter', 'pagsubok')

for line123 in contents.splitlines():
    print(line123)