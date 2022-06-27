import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/");
response.raise_for_status

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_title = [movie.get_text() for movie in movies]
movies_title =  movies_title[::-1]

# open file for writing
with open(file="topMovies.txt", mode="w") as fp:
    for movies in movies_title:
        fp.write(str(movies) + "\n")