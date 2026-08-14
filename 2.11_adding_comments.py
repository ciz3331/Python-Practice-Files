#name of program:
#2.7_stripping names

#What it does: it removes whitespaces on a string either from left,right, or both 

#code:
name = "\t\n\tCarlo James Justo\n\t\t\n"
print(f"no strip: {name}")

#left strip
print(f"left strip: {name.lstrip()}")
#right strip
print(f"right strip: {name.rstrip()}")
#strip both sides
print(f"strip both sides: {name.strip()}")


#name of program:
#file_extensions:

#What it does: it removes a part of txt, starting either from 
#left(.removeprefix()) or right(.removesuffix()). The part to be removed will be
#stated in the function's parameter. (e.g. removesuffix(".txt")). It works like
#lstrip() or rstrip() but needs a parameter and instead of removing whitespace,
#you can remove a specific part of the string.
#
#Note, both functions only check starting from left most side or right most
#side, if you're removing a part of string that's not in left most or rigth most
#side, it won't remove it.(e.g.python_note.txts
#                           print(filename.removesuffix(".txt"))
#                           Output: python_note.txts)

#code:
filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))