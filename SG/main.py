import json
import os
from bs4 import BeautifulSoup
import requests
from lxml import *
import re
import time


def website(new_links):
    # print(new_links)
    x = 0
    final_json_dict = []
    while x < 5:
        all_details = {}
        url = requests.get(new_links[x]).text
        soup = BeautifulSoup(url, "html.parser")
        all_details["Name:"] = soup.find("p", attrs={"data-testid": "new-listing-details-page-desktop-text-title"}).text
        all_details["Price:"] = soup.find(name= "div" , class_="D_Xo").text
        nope = soup.find(name="div", class_="D_hN")
        print("Condition , Mailing type ,Location is  : ")
        for things in nope.find_all(name="div", class_= "D_XL"):
            print(f"{things.text}:")
        try:
            all_details["details"] = soup.select_one(selector="section > div:nth-child(4) > div").text
        except:
            print("details are not available")
            pass
        try:
            all_details["reports"] = soup.select_one(selector="section > div:nth-child(5) > div").text
        except:
            print("condition report not available")
            pass
        try:
            all_details["Description"] = soup.select_one(selector="section > div:nth-child(7)").text
        except:
            print("description is not availabe")
            pass
        try:
            all_details["other details "] = soup.select_one(selector="section > div:nth-child(8) > div").text
        except:
            print("other details not available")
            pass
        x = x + 1
        final_json_dict.append(all_details)
        time.sleep(2)
    return json.dumps(final_json_dict, indent=4)


def main():
    search = input("what do u want to search for?")
    base_search = f"https://www.carousell.sg/search/{search}"
    base = "https://www.carousell.sg"

    url = requests.get(base_search).text
    soup = BeautifulSoup(url, "html.parser")
    products = soup.select("div.D_Kg.D__")
    number = 0
    new_links = []
    for product in products:
        x = product.find_all("div", class_="D_Kb D_LL")
        for link in x:
            ahem = link.find_all("a", href=True)

            for god in ahem:
                if number % 2 != 0:
                    nr = (god.get("href"))
                    number = number + 1
                    links = base + nr
                    new_links.append(links)
                else:
                    number = number + 1
                    continue

    json_string = website(new_links)
    with open("info.json", "w") as outfile:
        outfile.write(json_string)
    return


if __name__ == '__main__':
    main()
