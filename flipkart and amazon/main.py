import time
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# product name,price mrp, price discount percentage, discounted final price

s = Service(r"C:\Users\aftab\Dev\chromedriver.exe")


def amazon(search, driver):
    url = "https://www.amazon.in/"

    driver.get(url)
    try:
        driver.find_element(By.ID, value="twotabsearchtextbox").send_keys(search)
    except Exception as e:
        print(f"Error occured at find element twotabsearchtextbox \n{e.__str__()}")
        return

    try:

        driver.find_element(By.ID, value="nav-search-submit-text").click()
    except Exception as e:
        print(f"Error occured at find element nav-search-submit-text \n{e.__str__()}")
        return
        # getting the produscts from main page after search
    try:
        products = driver.find_elements(By.XPATH, value='//div[@data-component-type="s-search-result"]')
    except Exception as e:
        print(f"Error occured at find element //div[@data-component-type=s-search-result \n{e.__str__()}")
        return
    final_Products = []

    # if there are more than 1 classes in a single class , use xpath to ease your work

    count = 0
    for product in products:
        if count > 3:
            break

        final_Product = {}
        final_Product = defaultdict(lambda: "", final_Product)

        try:
            if product.find_element(By.CLASS_NAME, value="s-label-popover-default").text == "Sponsored":
                continue

        except:
            pass

        time.sleep(2)
        try:
            product.find_element(By.TAG_NAME, value="h2").click()
        except Exception as e:
            print(f"Error occured at find element h2 \n{e.__str__()}")
            continue
        time.sleep(2)

        try:
            driver.switch_to.window(driver.window_handles[1])
        except Exception as e:
            print(f"Error occured at find element (driver.window_handles[1]) \n{e.__str__()}")
            continue

        # time.sleep(2)
        name_list = []
        try:
            name_list = driver.find_elements(By.CSS_SELECTOR, value="h1 #productTitle")
        except Exception as e:
            print(f"Error occured at find element h1 #productTitle \n{e.__str__()}")
            continue

        for f in name_list:
            final_Product["name"] = f.text
        mrp_list = []
        try:
            mrp_list = driver.find_elements(By.CSS_SELECTOR,
                                            value="#apex_desktop div .a-color-secondary .a-text-price ")
        except Exception as e:
            print(f"Error occured at find element apex_desktop div \n{e.__str__()}")
            continue

        for f in mrp_list:
            final_Product["mrp"] = f.text
        Discounted_price = []
        try:
            Discounted_price = driver.find_element(By.XPATH, value='//span[@class="a-offscreen"]')
            # x = Discounted_price.text
        except Exception as e:
            print(f"Error occured at find element //span[@class=a-offscreen \n{e.__str__()}")
            continue

        x = Discounted_price.text
        final_Product["price"] = x.replace("\n", ".")
        final_Product["source"] = "Amazon"
        final_Products.append(final_Product)

        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        count = count + 1
    return final_Products


def find_fk_name(driver):
    element = driver.find_element(By.CSS_SELECTOR, value='h1.yhB1nd').text
    if element:
        return element
    else:
        return False


def find_fk_mrp(driver):
    element = driver.find_element(By.XPATH, value='//div[@class="_3I9_wc _2p6lqe"]').text
    if element:
        return element
    else:
        return False


def find_fk_price(driver):
    element = driver.find_element(By.XPATH, value='//div[@class="_30jeq3 _16Jk6d"]').text
    if element:
        return element
    else:
        return False


def flipkart(search, driver):
    url = "https://www.flipkart.com/"
    driver.maximize_window()
    driver.get(url)

    # time.sleep(5)
    try:
        driver.find_element(By.XPATH, value='//button[@class="_2KpZ6l _2doB4z"]').click()
    except:
        pass

    driver.find_element(By.XPATH, value='//input[@name="q"]').send_keys(search)

    driver.find_element(By.XPATH, value='//button[@class="L0Z3Pu"]').click()

    time.sleep(5)

    parentcontainer = driver.find_element(By.XPATH, value='//div[@class="_1YokD2 _2GoDe3"]')
    container = parentcontainer.find_element(By.XPATH, value='//div[@class="_1YokD2 _3Mn1Gg"]')
    all_products = container.find_elements(By.XPATH, value='//div[@class="_13oc-S"]')
    allfk_products = []
    count = 0
    while count < 3:
        for product in all_products:
            product.click()
            driver.switch_to.window(driver.window_handles[1])
            final_Product = {}
            final_Product = defaultdict(lambda: "", final_Product)
            final_Product["name"] = WebDriverWait(driver, 5).until(find_fk_name)
            final_Product["mrp"] = WebDriverWait(driver, 5).until(find_fk_mrp)
            final_Product["price"] = WebDriverWait(driver, 5).until(find_fk_price)
            final_Product["source"] = "Flipkart"
            allfk_products.append(final_Product)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            count = count + 1

        return allfk_products


def main():
    text = input("please enter search query:- \n")
    s = Service(r"C:\Users\aftab\Dev\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # print(flipkart(text, driver))
    final_Products = amazon(text, driver)
    final_Products += flipkart(text, driver)
    for final_Product in final_Products:

        to_print = "Product Info :\n\n"

        if len(final_Product['name']) > 0:
            to_print += f"Name : {final_Product['name']}\n"
        if len(final_Product['mrp']) > 0:
            to_print += f"Maximum Selling Price : {final_Product['mrp']}\n"
        if len(final_Product['price']) > 0:
            to_print += f"Current discounted Price : {final_Product['price']}\n"

        to_print += f"source : {final_Product['source']}\n\n"

        print(to_print)
    driver.quit()


if __name__ == '__main__':
    main()
