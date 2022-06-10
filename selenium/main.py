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
#                              value=".a-box-group #apex_offerDisplay_desktop #corePrice_feature_div .a-section .a-price-whole")
price = driver.find_elements(By.CSS_SELECTOR,
                             value="div.twister-plus-buying-options-price-data")


# god = json.loads(price)
# print(god)
#login_form = driver.find_element(By.XPATH, "/html/body/form[1]")

name_list = driver.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")
mrp_list = driver.find_elements(By.CSS_SELECTOR,
                                value="#apex_desktop div .a-color-secondary .a-text-price ")

# for f in mrp_list:
#     print(f"the current mrp is ", f.text)
#
# for h in name_list:
#     print(f"the name of product is ", h.text)

for x in price:
    print(f"the current price after discount is ", x.text)


driver.quit()