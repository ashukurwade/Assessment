# Many travel websites (e.g., Expedia, Skyscanner, Google Flights) display real-time flight prices that change frequently.
# Write a web scraper that:
#  Searches for flights between two cities (e.g., Mumbai - New York).
#  Extracts flight details (departure time, price).

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the search URL (example for a hypothetical website)
def get_search_url(origin, destination, date):
    base_url = "https://example-flights-website.com/search"
    return f"{base_url}?origin={origin}&destination={destination}&date={date}"

# Function to scrape flight data
def scrape_flights(origin, destination, date):
    # Get the search URL
    url = get_search_url(origin, destination, date)
    
    # Send a GET request to the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return []
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract flight details (adjust selectors based on the website's structure)
    flights = []
    for flight in soup.select(".flight-class"):  # Replace with the correct CSS selector
        departure_time = flight.select_one(".departure-time").text.strip()
        price = flight.select_one(".price").text.strip()
        flights.append({
            "Departure Time": departure_time,
            "Price": price
        })
    
    return flights

# Main function
if __name__ == "__main__":
    # Define search parameters
    origin = "Mumbai"
    destination = "New York"
    date = "2023-12-01"  # Format: YYYY-MM-DD
    
    # Scrape flight data
    flights = scrape_flights(origin, destination, date)
    
    # Display results in a DataFrame
    if flights:
        df = pd.DataFrame(flights)
        print(df)
    else:
        print("No flights found.")