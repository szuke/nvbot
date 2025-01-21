from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

import time

# svc = webdriver.ChromeService(executable_path=binary_path)

# Set up the WebDriver (Replace 'C:\Users\scott\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe' with the actual path)
# driver = webdriver.Chrome(executable_path='C:\Users\scott\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=svc)

driver = webdriver.Chrome(options= chrome_options)

# Navigate to the website
# driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-5090-32gb-gddr7-graphics-card-dark-gun-metal/6614151.p?skuId=6614151')
driver.get('https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-4060-ti-16gb-gddr6-pcie-gen-4-x16-graphics-card-with-dual-fan-black/6562415.p?skuId=6562415')

print(driver.title)

assert "NVIDIA" in driver.title

# # Search for the NVIDIA 5090
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('NVIDIA 5090')
# search_box.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(5)

# myElem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, "//*[contains(@data-sku-id, '6562415') and contains(@data-button-state, 'ADD_TO_CART')]"))
myElem = WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_element_located((By.XPATH, "//*[contains(@data-sku-id, '6562415') and contains(@data-button-state, 'ADD_TO_CART')]")))
myElem = WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.XPATH, "//*[contains(@data-sku-id, '6562415') and contains(@data-button-state, 'ADD_TO_CART')]")))

time.sleep(5)

myElem.click()

# # Add the item to the cart
# //div[contains(@id,'test')]
# add_to_cart_button = driver.find_element(By.XPATH, "//*[contains(@id, 'fulfillment-add-to-cart-button')]")
# add_to_cart_button = driver.find_element(By.XPATH, "//*[contains(@class, 'c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button')]")
# add_to_cart_button = driver.find_element(By.XPATH, "//*[contains(@data-sku-id, '6562415') and contains(@data-button-state, 'ADD_TO_CART')]")

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
