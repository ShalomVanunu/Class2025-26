import requests
from bs4 import BeautifulSoup

URL = "https://keithgalli.github.io/web-scraping/webpage.html"

url_content = requests.get(URL)
URL_content = url_content.text # HTML code

soup_data = BeautifulSoup(URL_content,"html.parser")

a_data = soup_data.find_all("img")


for link in a_data:
     print(link.get("src"))

#



