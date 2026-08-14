# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

while True:
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    
    try:
        add = int(num1) + int(num2)
    except ValueError as e:
        print(f"Can't add letters to a number! {type(e)}")
    else:
        print(f"{num1} + {num2} = {add}")