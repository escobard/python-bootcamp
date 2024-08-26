# scrape websites with beautiful soup - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

with open('website.html') as file:
  contents = file.read()

# sample of how to parse html elements
soup = BeautifulSoup(contents, 'html.parser')

# # sample of how to extract html elements from a site
# print(soup.title)
#
# # sample of how ot extract html content from element
# print(soup.title.string)
#
# # sample of how to prettify nesting of html content
# print(soup.prettify())

# sample of how to find all elements available with a particular tag
# creates a list of found elements
all_anchor_tags = soup.find_all(name="a")

# getText() grabs the text within a particular element
print(all_anchor_tags[0].getText())

# sample of how to find an element with a particular identifier
heading = soup.find(name="h1", id="name")

# sample of how to find an element by HTML class
section_heading = soup.find(name="h3", _class="heading")

# sample of how to get the content of an HTML element tag
print(section_heading.get("class"))

# sample of how to use css selectors to select one element - select() can be used to select all matching elements
company_url = soup.select_one(selector="p a")
print(company_url)