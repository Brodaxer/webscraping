import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_titles = [title.get_text() for title in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(title + "\n")
