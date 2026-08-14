# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

programming_words = {
    'list' : ('a list of one or more elements. Also called as array on most'
              ' programming languages.'),
    'value' : 'a.k.a. elements.',
    'variables' : 'are identifiers which contains a value.',
    'for loops' : ' are loops which format is (for temp_var in list:).',
    'tuples' : 'are immutable lists.',
    'range()' : ('takes parameters as numbers, you can use this to create lists'
                'automatically.'),
    'slice()' : ('are used in dictionaries and lists to take a specific part'
                 ' of it.'),
    'del' : ("A special type of keyword that de-references any object."
             "It's not a variable or function, it's a statement"),
    'not' : ("a keyword in python which equivalents to '!' in other languages"),
    'in/not in' : ('a keyword that typically access all the elements in a list'
                    ' or dictionary. The in/not in can also be used to check'
                    ' if a list is empty'),

}

for word, meaning in programming_words.items():
    print(f"{word.title()}\n\t-> {meaning}")