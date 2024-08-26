# scrape ycombinator

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

# returns the html of the page
# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# select first link on the page
# article_links = soup.select_one("td.title span.titleline a")
# article_score = soup.select_one("td.subtext span.score")
# article_links_text = article_links.getText()
# article_link_url = article_links.get("href")
# article_link_score = article_score.getText()

# place article links and score into lists
texts = []
links = []
article_links = soup.select("td.title span.titleline")
for article_link in article_links:
  top_link = article_link.select_one("a")
  text = top_link.getText()
  link = top_link.get("href")
  texts.append(text)
  links.append(link)

# place only score numbers into list with list comprehension
scores = [int(score.getText().split()[0]) for score in soup.select("td.subtext span.score")]

print(texts)
print(links)
print(scores)

# find title and link for the article with the highest votes
## max finds the largest number in a list of numbers
largest_number = max(scores)
## index finds the index position for a value
largest_index = scores.index(largest_number)
print(texts[largest_index], links[largest_index])
