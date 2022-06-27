import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")
titles = soup.find_all(name="a", class_="titlelink")

article_texts = []
article_links = []
for articleTag in titles:
    text = articleTag.get_text()
    article_texts.append(text)
    link = articleTag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
index_of_highes = article_upvote.index(max(article_upvote))

print(article_texts[index_of_highes])
print(article_links[index_of_highes])
print(article_upvote[index_of_highes])

