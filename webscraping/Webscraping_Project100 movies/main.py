import requests
from bs4 import BeautifulSoup

URL: str = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



# Write your code below this line 👇

response = requests.get(URL)
content = response.text

# parsing html with beautiful soup
soup = BeautifulSoup(content, "lxml")
all_movies = soup.find_all("h3", class_="title")


#extracting details from the website
movie_titles = [movie.text for movie in all_movies]
new_movie_list = movie_titles[::-1]
print(new_movie_list)


# writing the list into a file
with open("movies.txt", mode="w") as file:
    for movie in new_movie_list:
        file.write(f"{movie}\n")

