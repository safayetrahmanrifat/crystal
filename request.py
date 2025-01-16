from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your WebDriver (update with your path)
driver_path = "path/to/chromedriver"

# URL of the website
url = "https://yourwebsite.com"

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Loop to simulate multiple visits
for i in range(10):  # Adjust the range for more visits
    driver.get(url)  # Open the website
    print(f"Visit {i+1}: Opened {url}")
    time.sleep(5)  # Wait for 5 seconds to mimic browsing behavior

# Close the browser
driver.quit()
