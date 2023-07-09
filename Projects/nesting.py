# Nesting in python
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
}

# Nesting a list in a list
["A", "B", ["C", "D", "E"], "F"]

# Nesting dictionary in a dictionary
travel_logg = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Munich"], "total_visits": 9}
}

# Nesting a dictionary in a list
travel_loggg = [
    {
        "country": "France",
        "countries_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "countries_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visits": 5
    }
]


# Function to add content to the dictionary
def add_new_country(country_visited, cities_visited, times_visited):
    new_dict = {}
    new_dict["country"] = country_visited
    new_dict["total_visits"] = times_visited
    new_dict["countries_visited"] = cities_visited
    travel_loggg.append(new_dict)


# Check the dictionary
add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])
print(travel_loggg)
