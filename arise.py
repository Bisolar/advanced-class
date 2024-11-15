import requests
from bs4 import BeautifulSoup

url = "https://www.arise.tv/category/global/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

for article in articles:
    title = article.find('h3').text
    # print(title)
    
    url = article.find("a")
    if url:
        link = url.get("href")
        # print(link)
    