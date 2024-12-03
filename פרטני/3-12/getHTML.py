import requests


URL = "https://loginbruteforce.onrender.com/"

data = requests.get(URL).text

print(data)