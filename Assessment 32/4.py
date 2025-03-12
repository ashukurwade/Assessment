# Write a Python script to scrape book titles and prices
# from a website like books.toscrape.com.

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    # Loop through each book container to extract title and price
    for book in books:
        # Extract the book title
        title = book.h3.a['title']
        
        # Extract the book price
        price = book.find('p', class_='price_color').text
        
        # Print the title and price
        print(f"Title: {title}, Price: {price}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")