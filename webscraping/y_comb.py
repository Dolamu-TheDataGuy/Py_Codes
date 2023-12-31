from bs4 import BeautifulSoup
import requests

url:str = "https://news.ycombinator.com/"

response = requests.get(url)
# print(response.text)
yc_web_page = response.text

soup= BeautifulSoup(yc_web_page, "lxml")

articles = soup.find_all("span", class_="titleline")


article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.find("a").get("href")
    article_links.append(article_link)

  
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvote)