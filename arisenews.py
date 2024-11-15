import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS global_news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, url TEXT NOT NULL)
        """)

base_url = "https://www.arise.tv/category/global/"
page = 1


while True:
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    if not articles:
        break

    for article in articles:
        title = article.find('h3').text
    
        url = article.find("a")
        if url:
            link = url.get("href")

        cursor.execute('''
                   INSERT INTO global_news (title,url) 
                   VALUES (?,?)''', (title, link))

    print(f"Scraped page {page}")
    page += 1

conn.commit()
conn.close()