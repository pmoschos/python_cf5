# List of city names
cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# Filtering city names longer than 5 characters using filter and lambda
long_cities = filter(lambda city: len(city) > 5, cities)

# Capitalizing the filtered city names using map and lambda
cap_length_cities = list(map(lambda city: city.title(), long_cities))

# All in one line
# cap_length_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

# Printing the list of transformed city names
print("Capitalized Cities with more than 5 characters:", cap_length_cities)

# Using list comprehension to filter and capitalize city names
# cap_length_cities = [city.title() for city in cities if len(city) > 5]

# Printing the transformed list
print("Capitalized Cities with more than 5 characters:", cap_length_cities)
