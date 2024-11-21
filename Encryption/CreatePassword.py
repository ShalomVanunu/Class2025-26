import requests
from bs4 import BeautifulSoup


URL = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&amp;content-type=text/plain"

useragent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
site = requests.get(URL, headers=useragent).text
print(site)

