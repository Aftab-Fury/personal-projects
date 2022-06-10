from bs4 import BeautifulSoup
import requests
from websites import a


def main():
    base = 'https://archivists.xyz/'

    url = requests.get(base)
    archivists = url.text
    data = []
    next_four = []
    soup = BeautifulSoup(archivists, "html.parser")

    articles = soup.select(selector="tr span nobr a")
    for tag in articles:
        text = (tag.getText())
        data.append(text)
    my_new_url = [base + x for x in data]
    # print(my_new_url)
    x = 0
    a = []
    while x < 4:
        next_url = my_new_url[x]
        a.append(next_url)
        x = x + 1
    # print(data)
    value = major_website(a)
    god = sub_websites()
    # nr = next_website_link(value)
    print(f"For the first Webpage the values are as follows:-\n{value}")
    # print(a)
    my_next_url = [base + x for x in value]
    # a.append(my_next_url)
    # print(my_next_url)
    # a.extend(my_next_url)



def major_website(a):
    x = 0
    data = []
    while x < 4:
        url = requests.get(a[x])
        archivists = url.text

        soup = BeautifulSoup(archivists, "html.parser")

        articles = soup.select(selector="tr span nobr a")
        for tag in articles:
            text = (tag.getText())
            # if "Archivists" not in text:
            #     continue
            data.append(text)
        # my_new_url = [base + x for x in data]
        x = x + 1
    # print(data)
    return data

def sub_websites():
    x = 0
    data = []
    while x < 15:
        url = requests.get(a[x])
        archivists = url.text

        soup = BeautifulSoup(archivists, "html.parser")

        articles = soup.select(selector="tr span nobr a")
        for tag in articles:
            text = (tag.getText())
            # if "Archivists" not in text:
            #     continue
            data.append(text)
        # my_new_url = [base + x for x in data]
        x = x + 1
    print(f"From above the values of these sub websites are as follows{data} \n")
    with open("movies.txt", mode="w",  encoding="utf-8") as file:
        for x in data:
            file.write(f"{x}\n")
    return data




if __name__ == "__main__":
    main()