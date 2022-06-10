from bs4 import BeautifulSoup
import requests


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
    value = major_4_website(a)
    # god = next_website_link(a, value)
    # nr = next_website_link(value)
    # print(value)
    # print(a)
    my_next_url = [base + x for x in value]
    # a.append(my_next_url)
    # print(my_next_url)
    # a.extend(my_next_url)


def major_4_website(a):
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
    print(data)
    return data


# def next_website_link(a, value):
#     b = len(value)  # 15
#     print(b)
#     # print(value)
#     x = 0
#     while x <= 3:
#         d = a[0]
#         print(d)
#         x = x+1


if __name__ == "__main__":
    main()

