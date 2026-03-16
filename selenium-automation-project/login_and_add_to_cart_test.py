from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com")

# Wait for page to load
time.sleep(2)

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login
driver.find_element(By.ID, "login-button").click()

# Wait for products page
time.sleep(3)

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Wait
time.sleep(2)

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Wait
time.sleep(3)

print("Automation test completed successfully")

# Close browser
driver.quit()