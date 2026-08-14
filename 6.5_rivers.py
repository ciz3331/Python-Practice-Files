# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •
#  Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •
#  Use a loop to print the name of each river included in the dictionary.
# •
#  Use a loop to print the name of each country included in the dictionary.

major_rivers = {
    'amazon' : 'brazil',
    'nile' : 'egypt',
    'yangtze' : 'china',
}

print("Rivers with countries:")
for river, country in major_rivers.items():
    print(f"\tThe {river.title()} runs through {country.title()}.")
print()

print("Rivers:")
for river in major_rivers.keys():
    print('\t' +river.title())
print()

print("Countries:")
for country in major_rivers.values():
    print('\t' +country.title())