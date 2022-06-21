from bs4 import BeautifulSoup
import requests
import re

allNames = []


def returnTexts(url: str) -> [str]:
    url = requests.get(url)
    data = []
    soup = BeautifulSoup(url.text, "html.parser")
    articles = soup.select(selector="tr td span nobr a")
    for tag in articles:
        text_replaced = tag.text.replace("\\", "//")
        text = f"{url.url}/{text_replaced}"
        data.append(text)
        global allNames
        allNames.append(text_replaced)
    return data


def main():
    base = 'https://archivists.xyz'
    print("NODE 1\n")
    all_base1 = returnTexts(base)

    all_base2 = []
    all_base3 = []
    count = 0
    for x1 in all_base1:
        if count >= 4:
            count = 0
            break
        count += 1
        all_base2 += returnTexts(x1)

    for x1 in all_base2:
        if count >= 4:
            count = 0
            break
        count += 1
        all_base3 += returnTexts(x1)

    print(all_base3)
    for name in allNames:
        print(name)


if __name__ == "__main__":
    main()
