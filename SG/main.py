import json
import os
from bs4 import BeautifulSoup
import requests
from lxml import *
import re
import time


def website(new_links):
    print(new_links)
    x = 0
    final_json_dict = []
    while x < 5:
        all_details = {}
        url = requests.get(new_links[x]).text
        soup = BeautifulSoup(url, "html.parser")
        all_details["Name:"] = soup.find(attrs={"data-testid": "new-listing-details-page-desktop-text-title"}).text
        price = soup.find(class_= "D_GJ D_wl D_lh D_wn D_wq D_wt D_wu D_wj").text
        print(price)
        all_details["Condition"] = soup.select_one(
            selector=" div.D_iF > section > div > div > div > div:nth-child(1) > p").text
        all_details["Courier Type is"] = soup.select_one(
            selector=" div.D_iF > section > div > div > div > div:nth-child(2) > p").text
        all_details["Place is"] = soup.select_one(
            selector=" div.D_iF > section > div > div > div > div:nth-child(3) > p").text
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
    products = soup.select(selector="#root > div > div.D_H > div > div.D_R > main > div > div:nth-child(1) > div")
    count = 1
    new_links = []
    for link in products:
        while count <= 30:
            try:
                one_link = link.select_one(selector=f"div:nth-child({count}) > div > div.D_JS > a:nth-child(2)")
                count = count + 1
                x = one_link.get("href")
                links = base + x
                new_links.append(links)
            except:
                pass
    json_string = website(new_links)
    with open("info.json", "w") as outfile:
        outfile.write(json_string)
    return


if __name__ == '__main__':
    main()
