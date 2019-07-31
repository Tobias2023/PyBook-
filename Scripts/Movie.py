import requests
from bs4 import BeautifulSoup
from csv import writer

r = requests.get('https://www.rottentomatoes.com/browse/upcoming/')

soup = BeautifulSoup(html_doc, 'html.parser')

movies = soup.find_all(class_='movie_info')

for movie in movies:
    title = movie.find(class_='movieTitle').get_text().replace('/n', '')
    print(title)



# url = 'https://www.rottentomatoes.com/browse/upcoming/'
# response = requests.get(url)
