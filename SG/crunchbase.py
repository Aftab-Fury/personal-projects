import re
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def main():
    base = "https://www.crunchbase.com/organization/tesla-motors"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

    url = requests.get(base, headers=headers).text
    soup = BeautifulSoup(url, "html.parser")
    for link in soup.find_all('a',
                              attrs={'href': re.compile("^https://")}):
        # display the actual urls
        print(link.get('href'))


if __name__ == '__main__':
    main()
