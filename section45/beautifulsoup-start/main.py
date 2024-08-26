# scrape websites with beautiful soup - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

with open('website.html') as file:
  contents = file.read()

# sample of how to parse html elements
soup = BeautifulSoup(contents, 'html.parser')

# sample of how to extract html elements from a site
print(soup.title)

# sample of how ot extract html content from element
print(soup.title.string)

# sample of how to prettify nesting of html content
print(soup.prettify())