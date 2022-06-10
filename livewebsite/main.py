import gettext

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

Yc_webpage = response.text

soup = BeautifulSoup(Yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink", href=True)
article_texts = []
article_links = []
for tag in articles:
    text = (tag.getText())
    article_texts.append(text)
    link = (tag.get("href"))
    article_links.append(link)


# all_href_tags = soup.find_all(name="a", class_="titlelink", href=True)
# for href in all_href_tags:
#     print(href.get("href"))
#
upVote = [int(score.getText().split()[0])for score in soup.find_all(name="span", class_="score")]
max_score = max(upVote)
index = upVote.index(max_score)
print(article_texts[index])
print(article_links[index])
print(max_score)

# for score in all_score_tags:
#     print(int(score.getText().split()[0]))
#
# print(article_texts)
# print(article_links)
# print(upVote)
