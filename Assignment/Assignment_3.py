# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

# Searching for the first product
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("film")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

#

# Verifying that the search results page has loaded
assert "film" in driver.title

# Selecting the first product from the search results
product_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/a[2]/div/div[1]/img")
product_link.click()

# Waiting for the product details page to load
time.sleep(7)


# Adding the product to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# click on no thanks button for warranty coverage
no_thanks_film = driver.find_element("id","attachSiNoCoverage")
no_thanks_film.click()

# Waiting for the cart to update
time.sleep(5)





# Verifying that the product has been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "1"

# Going back to the search results page
driver.back()
time.sleep(4)

# Searching for the second product
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("DualSense")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Verifying that the search results page has loaded
assert "DualSense" in driver.title

# Selecting the second product from the search results
Dualsense_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div[1]/span/a/div/img")
Dualsense_link.click()

# Waiting for the product details page to load
time.sleep(5)

# Adding the product to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)


# Verifying that both products have been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "2"
# Opening the cart
cart_button = driver.find_element("id", "nav-cart")
cart_button.click()

# Waiting for the cart to load
time.sleep(5)

# Verifying that the cart page has loaded
assert "Amazon.ca Shopping Cart" in driver.title

# Closing the webdriver
driver.close()