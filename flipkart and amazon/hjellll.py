from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
import json
service = Service(r"C:\Users\aftab\Dev\chromedriver.exe")
# product name,price mrp, price discount percentage, discounted final price
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = r"C:\Users\aftab\Dev\chromedriver.exe"
# url = input("Enter URL :- \n ")
url = "https://www.amazon.in/"
search = input("Enter what you want to search")
driver = webdriver.Chrome(service=service)

# driver.get(url=input())
driver.get(url)

driver.find_element(By.ID, value="twotabsearchtextbox").send_keys(search)

driver.find_element(By.ID, value="nav-search-submit-text").click()
#getting the produscts from main page after search
products = driver.find_elements(By.XPATH, value='//div[@data-component-type="s-search-result"]')

# if there are more than 1 classes in a single class , use xpath to ease your work

count = 0

for product in products[:4]:
    # product.find_element(By.TAG_NAME, value="h2")
    final_Product = {}
    # print(product.find_element(By.CLASS_NAME, value="s-label-popover-default").text)
    # wait = WebDriverWait(driver, 10)

    product.find_element(By.TAG_NAME, value="h2").click()

    # WebDriverWait(driver, 10)



    driver.switch_to.window(driver.window_handles[1])

    name_list = driver.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")
    for f in name_list:
        final_Product["name"] = f.text

    mrp_list = driver.find_elements(By.CSS_SELECTOR,
                                    value="#apex_desktop div .a-text-price ")
    for f in mrp_list:
        final_Product["mrp"] = f.text

    Discounted_price = driver.find_element(By.CSS_SELECTOR, value="span.a-price")
    x = Discounted_price.text

    final_Product["price"] = x.replace("\n", ".")

    to_print = "Product Info :\n\n"

    if len(final_Product['name']) > 0:
        to_print += f"Name : {final_Product['name']}\n"
    if len(final_Product['mrp']) > 0:
        to_print += f"Maximum Selling Price : {final_Product['mrp']}\n"
    else:
        print("mrp is not available")
    if len(final_Product['price']):
        to_print += f"Current discounted Price : {final_Product['price']}"

    print(to_print)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # count = count+1

driver.quit()

