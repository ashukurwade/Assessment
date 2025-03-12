# 2. Many company websites have a "Careers" page listing open job positions.
# Write a script to scrape job titles from a company's career page without using an API.

import requests
from bs4 import BeautifulSoup

# URL of the company's career page
url = "https://www.amazon.jobs/en/search?base_query=remote"  # Replace with the actual URL

# Send a GET request to the career page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all job titles (adjust the selector based on the website's structure)
    # Example: If job titles are in <h2> tags with class "job-title"
    job_titles = soup.find_all("h3", class_="info first col-12 col-md-8")  # Update the tag and class as needed

    # Extract and print the job titles
    if job_titles:
        print("Job Titles:")
        for title in job_titles:
            print(title.text.strip())
    else:
        print("No job titles found. Check the HTML structure and update the selector.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")