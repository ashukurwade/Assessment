# You're building an application that requires calculating the distance between a user's current location
# and various destinations. How would you use the Geopy library to handle this,
# and what considerations would you take into account for optimizing performance if there are thousands of destinations to compare?

from geopy.distance import geodesic
import pandas as pd

# User's current location (latitude, longitude)
user_location = (28.6139, 77.2090)  # Example: New Delhi, India

# Sample data (could be loaded from a CSV or database)
destinations = [
    {"name": "Taj Mahal", "latitude": 27.1751, "longitude": 78.0421},
    {"name": "Gateway of India", "latitude": 18.9220, "longitude": 72.8347},
    {"name": "India Gate", "latitude": 28.6129, "longitude": 77.2295},
    {"name": "Mysore Palace", "latitude": 12.3052, "longitude": 76.6551},
    {"name": "Charminar", "latitude": 17.3616, "longitude": 78.4747},
]

# Convert to Pandas DataFrame
df = pd.DataFrame(destinations)

# Calculate distances and add a new column
df["distance_km"] = df.apply(lambda row: geodesic(user_location, (row["latitude"], row["longitude"])).km, axis=1)

# Sort by nearest destinations
df_sorted = df.sort_values(by="distance_km")

# Display results
print(df_sorted)
