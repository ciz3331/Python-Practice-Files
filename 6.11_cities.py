# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    'tokyo' : {
        'population' : '14 million',
        'interesting fact' : ('Tokyo is known for its efficient public' 
                              ' transportation system, including the famous' 
                              ' Shinkansen (bullet train) network.'),
    },

    'rio de janeiro' : {
        'population' : '6.7 million',
        'interesting fact' : ('Rio de Janeiro is home to the iconic Christ the '
                            'Redeemer statue, one of the New Seven Wonders of '
                            'the World.'),
    },

    'dubai' : {
        'population' : '3.3 million',
        'interesting fact' : ('Dubai is renowned for its futuristic '
                              "architecture, including the world's tallest "
                              'building, the Burj Khalifa.'),
    },
}

for city, info in cities.items():
    print(f"{city.title()}")
    print(f"\tPopulation is approximately: {info['population'].title()}")
    print(f"\tOne interesting fact is {info['interesting fact']}")




        