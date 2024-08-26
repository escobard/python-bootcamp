# scrape movie data from empireonline, generate txt file with each movie's title in order

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_movies = response.text

soup = BeautifulSoup(empire_movies, 'html.parser')

title_list = ([title.getText() for title in soup.select("div.block-item h3")])

with open("movie_titles.txt", "w") as txt_file:
  for title in reversed(title_list):
    txt_file.write("".join(title) + "\n")