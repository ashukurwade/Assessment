from geopy.distance import geodesic

cities = [
    {"name": "New York", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "Los Angeles", "latitude": 34.0522, "longitude": -118.2437},
    {"name": "London", "latitude": 51.5074, "longitude": -0.1278},
    {"name": "Tokyo", "latitude": 35.6895, "longitude": 139.6917},
    # Add more cities as needed
]

max_distance = 0
city1, city2 = None, None

for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        coord1 = (cities[i]["latitude"], cities[i]["longitude"])
        coord2 = (cities[j]["latitude"], cities[j]["longitude"])
        distance = geodesic(coord1, coord2).kilometers

        if distance > max_distance:
            max_distance = distance
            city1, city2 = cities[i], cities[j]

print(f"The two cities farthest apart are {city1['name']} and {city2['name']} with a distance of {max_distance:.2f} kilometers.")