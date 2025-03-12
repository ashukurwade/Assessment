from geopy.distance import geodesic

# Define the two locations as tuples of (latitude, longitude)
location1 = (90, 0)  # North Pole
location2 = (-90, 0)  # South Pole

# Calculate the distance
distance = geodesic(location1, location2).kilometers  # Distance in kilometers
print(f"The straight-line distance between the two locations is {distance:.2f} kilometers.")
#############################
try:
    distance = geodesic(location1, location2).kilometers
    print(f"The straight-line distance between the two locations is {distance:.2f} kilometers.")
except ValueError as e:
    print(f"Invalid coordinates: {e}")