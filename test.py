from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the page
    driver.get("https://clublocker.com/teams/40867/results")

    # Wait for the page to load the dynamic content
    time.sleep(5)  # Adjust this delay as necessary

    # Find all elements containing team names and results
    matches = driver.find_elements(By.CSS_SELECTOR, "span.mat-button-wrapper")

    # Extract and print the text from each element
    for match in matches:
        print(match.text)

finally:
    # Close the WebDriver
    driver.quit()
