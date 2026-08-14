import random
#alphabet:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet)
print('')
#///////////////////////////////////////////////////////////////////////////////
#add 0-4 to end of alphabet list using append:
print("add 0-4 to end of alphabet list using append:")
alphabet.append('0')
alphabet.append('1')
alphabet.append('2')
alphabet.append('3')
alphabet.append('4')

print(alphabet)
print('')

#///////////////////////////////////////////////////////////////////////////////
#using .insert():
print('using .insert():')

#insert 5 to first index:
print("insert 5 to first index:")
alphabet.insert(0,'5')
print(alphabet)

#insert 6 to middle of list:
print("insert 6 to middle of list:")
mid = int(len(alphabet)/2)
alphabet.insert(mid,'6')
print(alphabet)

#insert 7 to second to the last element of list using -1:
print("insert 7 to second to the last element of list using -1:")
alphabet.insert(-1,'7')
print(alphabet)

#insert 8 to end of the list using len():
print("insert 8 to end of the list using len():")
length_of_list = len(alphabet)
alphabet.insert(length_of_list, '8')
print(alphabet)

#append() 9:
print("append() 9:")
alphabet.append('9')
print(alphabet)

print('')

#///////////////////////////////////////////////////////////////////////////////
#using del list[index#]:
print("using del list[index#]:")
print("delete end of list using del")
del alphabet[-1]
print(alphabet)
print('')

#///////////////////////////////////////////////////////////////////////////////
#using .pop(index#):
print("using .pop(index#):")

print("use pop() without index to remove last item on list, then print the\
 removed item")
last_item = alphabet.pop()
print(alphabet)
print("removed last item: " +last_item)

print("use pop to delete the middle element of the list, then print the removed\
 item: ")
mid_index = int(len(alphabet)/2)
mid_element = alphabet.pop(mid_index)
print(alphabet)
print("removed middle item: " +mid_element)
print('')

#///////////////////////////////////////////////////////////////////////////////
#using .remove(value)
print("using .remove(value) to delete the value 6:")
alphabet.remove('6')
print(alphabet)

print("used .append() twice to add 6")
alphabet.append('6')
alphabet.append('6')
print(alphabet)
print("used .remove() to remove 6, notice it only removed the first 6 on the\
 list")
alphabet.remove('6')
print(alphabet)
print('')

#//////////////////////////////////////////////////////////////////////////////
#using .sort() to sort list permanently:
print("using .sort() to sort list permanently: ")
alphabet.sort()
print(alphabet)
print('')

'''
#tested sort and sorted behaviour on special chars.
alphabet.append('!')
alphabet.append('@')
#alphabet.sort()
print(sorted(alphabet))
'''

#//////////////////////////////////////////////////////////////////////////////
#using random.shuffle(list) to shuffle the list randomly:
print("using random.shuffle(list) to shuffle the list randomly:")
random.shuffle(alphabet)
print(alphabet)
print('')

#//////////////////////////////////////////////////////////////////////////////
#using sorted(list) to sort list temporarily:
print("using sorted(list) to sort list temporarily:")
print(sorted(alphabet))

#checking sorted behavior on assigning list variable and using sorted on 1 statement
#this part is fucked up, ignore
print("checking sorted behavior on assigning list variable and using sorted on\
 1 statement #this part is fucked up, ignore")
alphabet2 = alphabet.copy()
print(alphabet2)
print("shuffling alphabet2: ")
random.shuffle(alphabet2)
print(alphabet2)
alphabet3 = alphabet2.copy()
alphabet.sort()
print(alphabet3)
print(f"Here's the existing alphabet list:\n {alphabet}")
print('')

#//////////////////////////////////////////////////////////////////////////////
#using .reverse():
print("using .reverse():")
print("Here's existing alphabet lists: ")
print(f"alphabet: {alphabet}")
print(f"alphabet2: {alphabet2}")
#shuffling alphabet3 since it's the same order as alphabet2
random.shuffle(alphabet3)
print(f"alphabet3: {alphabet3}")
print("reversed lists: ")
alphabet.reverse()
print(f"alphabet reversed: {alphabet}")
alphabet2.reverse()
print(f"alphabet2 reversed: {alphabet2}")
alphabet3.reverse()
print(f"alphabet3 reversed: {alphabet3}")
print('')

#//////////////////////////////////////////////////////////////////////////////
#using the argument (reverse=True) for .sort() and sorted():
print("using the argument (reverse=True) for .sort() and sorted():")
print("using reverse=True on alphabet for .sort()")
alphabet.sort(reverse=True)
print(alphabet)
print("using reverse=True on alphabet2 for sorted()")
print(sorted(alphabet2,reverse=True))


#testing upper/lower case behaviour of .sort() and sorted():
print("testing upper/lower case behaviour of .sort() and sorted():")
alphabet.append('A')
alphabet.append('B')
alphabet.sort()
print(alphabet)





