#alphabet:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("try to use .insert() on index# 69 which does not exist on this list:")
alphabet.insert(69,'69')
print(alphabet)

'''
print("try to del index# 69 which does not exist on this list: ")
del alphabet[69]
#error: IndexError: list assignment index out of range
'''

'''
print("try to remove 96, a non-existent value on the list: ")
alphabet('96')
alphabet.remove('96')
#error: TypeError: 'list' object is not callable
'''
