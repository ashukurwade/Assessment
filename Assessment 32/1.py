# Scrape product names name prices from an e-commerce website (like Flipkart, Amazon, or eBay).
# Since these websites use JavaScript,
# how would you extract data when it's not available in the page source?

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Selenium WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Navigate to the product page
url = "https://www.flipkart.com/search?q=watch&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
driver.get(url)

# Wait for the page to load (you can use explicit waits for better reliability)
time.sleep(5)

# Extract product names and prices
products = driver.find_elements(By.CLASS_NAME, 'WKTcLC')
prices = driver.find_elements(By.CLASS_NAME, 'Nx9bqj')

# Print the data
for product, price in zip(products, prices):
    print(f"Product: {product.text}, Price: {price.text}")

# Close the browser
driver.quit()