import requests
from bs4 import BeautifulSoup

url = "https://www.tvcnews.tv/world-news/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')      # Note: we have both html and lxml
for data in soup.find_all("article"):
    title = data.find("h3")
    print(title.text)

    url = data.find("a")
    if url:
        link = url.get("href")
        print(link)

    image = data.find("img")
    if image:
        img_url = image.get("src")
        print(img_url)
    else:
        print("No image found")

    print("\n")

    # Scrape the entire world news from arise news tvand save in a databased format 
    # https://www.arise.tv/category/global/
    # Scrape all 267 pages