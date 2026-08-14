# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city, country):
    return (f"{city.title()}, {country.title()}")

#Sydney, Australia
print(city_country('sydney', 'australia'))

#Vancouver, Canada
print(city_country('vancouver', 'canada'))

#Cairo, Egypt
print(city_country('cairo', 'egypt'))

