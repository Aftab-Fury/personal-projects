from bs4 import BeautifulSoup

# with open("website.html") as file:
#     contents = file.read()
contents = open("website.html", encoding="utf8")

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))
#     print(tag.getText())
company_url = soup.select(selector = "a")
print(company_url)
heading  = soup.find_all("h1", id="name")