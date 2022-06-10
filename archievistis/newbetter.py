from bs4 import BeautifulSoup
import requests
import re


def returnTexts(url: str) -> [str]:
    url = requests.get(url)
    data = []
    soup = BeautifulSoup(url.text, "html.parser")
    articles = soup.select(selector="tr td span nobr a")
    for tag in articles:
        text_replaced = tag.text.replace("\\", "//")
        only_text = tag.getText()
        text = f"{url.url}/{text_replaced}"
        # print(text)
        data.append(text)
        print(only_text)
    return data


def main():
    base = 'https://archivists.xyz'
    print("NODE 1\n")
    allBase1 = returnTexts(base)
    allbase2 = []
    allbase3 = []
    count = 0
    for x1 in allBase1:
        if count >= 4:
            count = 0
            break
        count += 1
        allbase2 += returnTexts(x1)

    for x1 in allbase2:
        if count >= 4:
            count = 0
            break
        count += 1
        allbase3 += returnTexts(x1)

    # print(allbase3)

if __name__ == "__main__":
    main()
