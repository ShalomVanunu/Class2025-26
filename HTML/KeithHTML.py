import requests

URL = "https://keithgalli.github.io/web-scraping/webpage.html"

url_content = requests.get(URL)

URL_content = url_content.text

URL_content_lines = url_content.text.split("\n")

for line in URL_content_lines:
    if "href" in line:
        print(line)


