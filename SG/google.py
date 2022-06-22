import re
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

import numpy as np


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua


user_agent = get_random_ua()
headers = {
    'user-agent': user_agent,
}
base = "https://www.crunchbase.com/organization/tesla-motors"
r = requests.get(base, headers=headers)
url = requests.get(base, headers=headers).text
soup = BeautifulSoup(url, "html.parser")
for link in soup.find_all('a',
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href'))