# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary
# variable, lines, to show how splitlines() works. You can skip the temporary
# variable and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section,
# to make them more concise.

from pathlib import Path

#file_reader.py
path = Path('pi_digits.txt')
contents = path.read_text()
#lines = contents.splitlines()

for line in contents.splitlines():
    print(line)


#pi_string.py
path = Path('pi_digits.txt')
contents = path.read_text()

pi_string = ''

for line in contents.splitlines():
    line = line.strip()
    pi_string += line

print(pi_string)
print(len(pi_string))