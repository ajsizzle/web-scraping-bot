import requests
from bs4 import BeautifulSoup

# Set URL to website you would like to scrape
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Change variable names so it makes more sense to the project you are scraping
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

# Sends information to .txt file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

