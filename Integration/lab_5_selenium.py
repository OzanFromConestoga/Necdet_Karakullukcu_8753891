# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("framed wall art")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(4)

# Verifying that the search results page has loaded
assert "framed wall art" in driver.title

# Selecting shoes from the search results
# laptop_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
shoes_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/a/div/img")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
shoes_link.click()

time.sleep(5)

# Selecting shoes size from the dropdown menu
quantity = driver.find_element("id","quantity")

quantity.click()

# Locate your mouse to click the correct size of shoes
locate_quantity = driver.find_element("xpath","/html/body/div[2]/div[2]/div[4]/div[4]/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[7]/div/div/span/div/div/span/select/option[5]")

time.sleep(2)

locate_quantity.click()

# Waiting for the shoes details page to load
time.sleep(3)

# Verifying that the correct shoes details page has loaded
# assert "shoes" in driver.title

# Adding shoes to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on go to cart button
#goto_cart= driver.find_element("id","rpn4f7-iqc02o-yu0rej-96teta")
#goto_cart.click()
#time.sleep(3)

# Verifying that shoes have been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "1"

# Closing the webdriver
driver.close()
