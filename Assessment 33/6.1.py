# Assume you have a dataset of cities, each with latitude and longitude coordinates.
# How would you utilize Geopy to find the nearest city to a given location? Also, how would you handle edge cases,
# such as cities on the other side of the world or cities that fall on the same latitude or longitude line?

from geopy.distance import geodesic

given_latitude = 37.7749
given_longitude = -122.4194
given_location = (given_latitude, given_longitude)

# dataset of cities
cities = [
    {'name': 'City A', 'latitude': 34.05, 'longitude': -118.25},
    {'name': 'City B', 'latitude': 40.71, 'longitude': -74.01},
    {'name': 'City C', 'latitude': 51.51, 'longitude': -0.13},
]

# Function to find the nearest city
def find_nearest_city(given_location, cities):
    nearest_city = None
    min_distance = float('inf')
    
    for city in cities:
        city_location = (city['latitude'], city['longitude'])
        distance = geodesic(given_location, city_location).kilometers
        
        if distance < min_distance:
            min_distance = distance
            nearest_city = city
    
    return nearest_city, min_distance

# Find the nearest city
nearest_city, distance = find_nearest_city(given_location, cities)

print(f"The nearest city is {nearest_city['name']} with a distance of {distance:.2f} kilometers.")