from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# product name,price mrp, price discount percentage, discounted final price


chrome_driver_path = r"C:\Users\aftab\Dev\chromedriver.exe"
url = input("Enter URL :- \n ")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(url=input())
driver.get(url)

# price = driver.find_elements(By.CSS_SELECTOR,
#                              value="span.a-price")
price = driver.find_element(By.CSS_SELECTOR, value="span.a-price")
# price = driver.find_elements(By.XPATH, value="/div/div/div/form/div/div/div/div/div/div/div")

# god = json.loads(price)
# print(god)
# login_form = driver.find_element(By.XPATH, "/html/body/form[1]")

name_list = driver.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")
mrp_list = driver.find_elements(By.CSS_SELECTOR,
                                value="#apex_desktop div .a-color-secondary .a-text-price ")
final_Product = {}
for f in mrp_list:
    final_Product["mrp"] = f.text

for f in name_list:
    final_Product["name"] = f.text

x = price.text

final_Product["price"] = x.replace("\n", ".")


to_print = "Product Info :\n\n"

if len(final_Product['name']) > 0:
    to_print += f"Name : {final_Product['name']}\n"
if len(final_Product['mrp']) > 0:
    to_print += f"Maximum Selling Price : {final_Product['mrp']}\n"
if len(final_Product['price']):
    to_print += f"Current discounted Price : {final_Product['price']}"

print(to_print)

driver.quit()