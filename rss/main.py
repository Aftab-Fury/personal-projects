import feedparser

NewsFeed = feedparser.parse("https://nyaa.si/?page=rss")
f=0
big_string = " "
for x in NewsFeed.entries:
    if f>=10:
        break
    f= f+1
    big_string += f"Title is {x.title}\nId is {x.id}\n\n"
print(big_string)