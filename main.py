from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

import time

# svc = webdriver.ChromeService(executable_path=binary_path)

# Set up the WebDriver (Replace 'C:\Users\scott\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe' with the actual path)
# driver = webdriver.Chrome(executable_path='C:\Users\scott\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=svc)

driver = webdriver.Chrome(options= chrome_options)

# Navigate to the website
driver.get('https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-4090-gaming-oc-24gb-gddr6x-pci-express-4-0-graphics-card-black/6521518.p?skuId=6521518')

print(driver.title)

assert "NVIDIA" in driver.title

# # Search for the NVIDIA 5090
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('NVIDIA 5090')
# search_box.send_keys(Keys.RETURN)

# # Wait for the results to load
# time.sleep(3)

# # Add the item to the cart
# add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
# add_to_cart_button.click()

# # Proceed to checkout
# checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout-button"]')
# checkout_button.click()

# # Enter shipping and payment details here

# # Place the order
# place_order_button = driver.find_element(By.XPATH, '//*[@id="place-order-button"]')
# place_order_button.click()

# Close the browser
# driver.quit()
