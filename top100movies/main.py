import gettext

from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
top100 = response

soup = BeautifulSoup(response, "html.parser")
articles = soup.find_all(name= "h3" , class_= "title")
article_texts = []

for tag in articles:
    text = (tag.getText())
    article_texts.append(text)

article_texts.reverse()
# for text in article_texts:
#     print(text)

with open("movies.txt", mode="w") as file:
    for x in article_texts:
        file.write(f"{x}\n")