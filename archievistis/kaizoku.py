from bs4 import BeautifulSoup
import requests


def main():
    links = []
    kaizoku = 'https://animekaizoku.com/'
    url = requests.get(kaizoku)
    animekaisoku = url.text
    soup = BeautifulSoup(animekaisoku, "html.parser")
    # till here we have created only the soup
    # now we will find the exact liknk and name of the x element
    x_element = soup.select(selector="div div div h3")
    # getting names of the subtitles only
    for tag in x_element[:4]:
        # names of subtitles
        text = (tag.getText())
        print(text)
    # getting href now for the first 4
    h_element = soup.select(selector="div div div h3 a")
    for tag in h_element[:4]:
        href = tag.get("href")
        links.append(href)
    my_new_url = [kaizoku + f for f in links]
    x = len(my_new_url)
    # print(x)
    things_in_the_url(my_new_url, x)
    # print(my_new_url)


def things_in_the_url(my_new_url, x):
    y = int(x)
    # print(y)
    while y >= 0:
        url = requests.get(my_new_url[y-1])
        animekaisoku = url.text
        soup = BeautifulSoup(animekaisoku, "html.parser")
        # heading = soup.select(selector="tbody tr td")
        # for tags in heading:
        #     text = tags.getText()
        #     print(text)

        n_element = soup.select(selector="tr td a")

        for tags in n_element:
            text = (tags.getText())
            print(text)
        y = y - 1


if __name__ == "__main__":
    main()
