from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import defaultdict


# product name,price mrp, price discount percentage, discounted final price

class Amazon:
    def __int__(self, driver, text):
        self.d = driver
        self.search = text

    def getmrp(self):
        return self.d.find_elements(By.CSS_SELECTOR,
                                    value="#apex_desktop div .a-color-secondary .a-text-price ")

    def getname(self):
        return self.d.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")

    def getprice(self):
        return self.d.find_elements(By.XPATH, value='//span[@class="a-offscreen"]')


def main():
    chrome_driver_path = r"C:\Users\aftab\Dev\chromedriver.exe"
    url = input("Enter URL :- \n")
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    final_Product = {}
    final_Product = defaultdict(lambda: "", final_Product)

    driver.get(url)

    price = driver.find_elements(By.XPATH, value='//span[@class="a-price-whole"]')
    name_list = driver.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")
    mrp_list = driver.find_elements(By.CSS_SELECTOR,
                                    value="#apex_desktop div .a-color-secondary .a-text-price ")
    for f in mrp_list:
        final_Product["mrp"] = f.text

    for f in name_list:
        final_Product["name"] = f.text

    for f in price:
        final_Product["price"] = f.text

    to_print = "Product Info :\n\n"

    if len(final_Product['name']) > 0:
        to_print += f"Name : {final_Product['name']}\n"
    if len(final_Product['mrp']) > 0:
        to_print += f"Maximum Selling Price : {final_Product['mrp']}\n"
    if len(final_Product['price']) > 0:
        to_print += f"Current discounted Price :{final_Product['price']}"

    print(to_print)


    amazon = Amazon(driver, url)
    print(amazon.getprice(), amazon.getmrp(), amazon.getname())

    driver.quit()


if __name__ == '__main__':
    main()