# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a number.

#Author might meant 10.6, I did it already with while loop

while True:
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    
    try:
        add = int(num1) + int(num2)
    except ValueError as e:
        print(f"Can't add letters to a number! {type(e)}")
    else:
        print(f"{num1} + {num2} = {add}")