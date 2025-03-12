from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Path to your ChromeDriver
chrome_driver_path = "/path/to/chromedriver"

# Initialize the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the dynamic website
url = "https://www.amazon.in/All-Product/s?k=All+Product"

# Open the website
driver.get(url)

# Wait for the dynamic content to load
time.sleep(5)  # Adjust the sleep time based on the website's loading speed

# Extract product data
products = driver.find_elements(By.CLASS_NAME, "product")  # Replace with the correct class name

for product in products:
    name = product.find_element(By.CLASS_NAME, "product-name").text  # Replace with the correct class name
    price = product.find_element(By.CLASS_NAME, "product-price").text  # Replace with the correct class name
    print(f"Product: {name}, Price: {price}")

# Close the browser
driver.quit()