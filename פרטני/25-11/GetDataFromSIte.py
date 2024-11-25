import requests
from setuptools.package_index import user_agent

URL= "https://ksp.co.il/web/cat/31635..573"

user_agentt = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

site_content = requests.get(URL,user_agentt).text

print(site_content)