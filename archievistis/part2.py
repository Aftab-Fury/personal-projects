from bs4 import BeautifulSoup
import requests


def main():
    base = 'https://archivists.xyz/'

    url = requests.get(base)
    archivists = url.text
    data = []
    next_for = []
    soup = BeautifulSoup(archivists, "html.parser")

    articles = soup.find_all("a", href=True)

    articles = soup.select(selector="tr td span nobr a")
    urls = []

    for tag in articles:
        link = tag.get("href")
        urls.append(link)
    for tag in articles:
        text = (tag.getText())
        if "Archivists" not in text:
            continue
        data.append(text)
    my_new_url = [base + x for x in data]
    # print(my_new_url)
    x = 0
    a = []
    # while x < 4:
    #     next_url = my_new_url[x]
    #     a.append(next_url)
    #     x = x + 1
    print(data)
    a = [base + x for x in urls]
    value = major_4_website(a)
    next_url(my_new_url)
    hod = true(a)
    for x in hod:
        a.append(hod)
    # print(value)
    # print(hod)
    # print(a)
    # print(a)


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
            data.append(text)
        # my_new_url = [base + x for x in data]
        x = x + 1
        # print(data)
        # print(data)
    # print(data)
    return data


def true(a):
    x = 0
    arch = 'https://archivists.xyz/'
    base = a
    urls = []
    while x <= 3:
        url = requests.get(base[x])
        archivists = url.text
        soup = BeautifulSoup(archivists, "html.parser")

        articles = soup.find_all("a", href=True)

        articles = soup.select(selector="tr td span nobr a")
        x = x + 1

        for tag in articles:
            link = tag.get("href")
            urls.append(link)
    my_new_url = [arch + f for f in urls]
    ahem = next_url(my_new_url)
    # print(my_new_url)
    return my_new_url


def next_url(my_new_url):
    x = 0
    data = []
    while x < 4:
        url = requests.get(my_new_url[x])
        archivists = url.text

        soup = BeautifulSoup(archivists, "html.parser")

        articles = soup.select(selector="tr span nobr a")
        for tag in articles[:4]:
            text = (tag.getText())
            data.append(text)
        # my_new_url = [base + x for x in data]
        x = x + 1
        # print(data)
        # print(data)
    print(data)
    return data


if __name__ == "__main__":
    main()
