import requests
from bs4 import BeautifulSoup

r = requests.get('https://ge.globo.com/')
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title)

get_news = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')

for title in get_news:
    print(title.text)


blog_titles = soup.select(a.feed-post-link gui-color-primary gui-color-hover)
# class="feed-post-link gui-color-primary gui-color-hover"
for title in blog_titles:
    print(title.text)