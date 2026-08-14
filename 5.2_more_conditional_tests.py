# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them 
# to conditional_tests.py. Have at least one True and one False result for each of 
# the following:

#ests for equality and inequality with strings
cj = 'pogi'
print("Is cj == 'pogi'? I predict True")
print(cj == 'pogi')

print("Is cj == 'panget'? I predict False")
print(cj == 'panget')

#tests using the lower() method
cj_full_name = 'Carlo James Castro Justo'
print("Is cj_full_name == 'Carlo James Castro Justo'? I predict True")
print(cj_full_name.lower() == 'carlo james castro justo')

print("Is cj_full_name == 'Carlo James Justo'? I predict False")
print(cj_full_name.lower() == 'carlo james justo')

# Numerical tests involving equality and inequality, greater than and less 
#than, greater than or equal to, and less than or equal to
#== and !=
sixty_nine = 69
print("Is sixty_nine == 69? I predict True")
print(sixty_nine == 69)

print("Is sixty_nine == 70? I predict False")
print(sixty_nine == 70)

print("Is sixty_nine != 71? I predict True")
print(sixty_nine != 71)

print("Is sixty_nine != 69? I predict False")
print(sixty_nine != 69)

#> and <
print("Is 1 > -1? I predict True")
print(1 > -1)

print("Is -1 > 1? I predict False")
print(-1 > 1)

print("-69 < 69? I predict True")
print(-69 < 69)

print("Is 69 < -69? I predict False")
print(69 < -69)

#>= and <=
legal = 18
print("Is legal >= 18? I predict True")
print(legal >= 18)

print("Is legal >= 19? I predict False")
print(legal >= 19)

print("Is legal <= 18? I predict True")
print(legal <= 18)

print("Is legal <= 16? I predict False")
print(legal <= 16)

#Tests using the and keyword and the or keyword
#and
print("Is #True:(legal > 17) and #True:(legal < 19)? I predict True")
print((legal > 17) and (legal < 19))

print("Is #True:(legal > 17 and #False:(legal > 19)? I predict False")
print((legal > 17) and (legal > 19))

#or
print("Is #True:(legal > 17) or #False:(legal < 17)? I predict True")
print((legal > 17) or (legal < 17))

print("Is #False:(legal < 17) or #False:(legal < 16)? I predict False")
print((legal < 17) or (legal < 16))

#Test whether an item is in a list
dodge_models = ['attitude', 'charger', 'durango', 'hornet', 'journey']
#True element 'in' list
print("Is charger in dodge_models? I predict True")
print('charger' in dodge_models)

#False element 'in' list
print("Is ninja in dodge_models? I predict False")
print('ninja' in dodge_models)

#Test whether an item is not in a list
#True element 'not in' list
print("Is diavel not in dodge_models? I predict True")
print('diavel' not in dodge_models)

#False element 'not in' list
print("Is hornet not in dodge-models? I predict False")
print('hornet' not in dodge_models)