
import requests
from bs4 import BeautifulSoup

url = "https://www.ceicdata.com/en/indicator/israel/population"

page_html_contet = requests.get(url).text

bs_page = BeautifulSoup(page_html_contet,"html.parser")

a_href = bs_page.find_all("a")

county_lst =[]

for country in a_href:
    county_lst.append(country.get_text("href").strip())
#print(county_lst.index("Albania (Person mn)"))
for country in county_lst[38:138]:
    print(country)
