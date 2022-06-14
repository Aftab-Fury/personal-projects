import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

s = Service(r"C:\Users\aftab\Dev\chromedriver.exe")




def find_name(driver):
    element = driver.find_element(By.CSS_SELECTOR, value='h1.yhB1nd').text
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

    for product in all_products:
        product.click()
        driver.switch_to.window(driver.window_handles[1])
        element = WebDriverWait(driver, 5).until(find_name)
        print(element)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


if __name__ == '__main__':
    main()