
import requests

URL = "https://hack-yourself-first.com/"

url_content = requests.get(URL)

url_content_post = requests.post(URL,{"Email":"shalom@gmail.com","password":" "})

if "Login" not in url_content_post.text: # check Home page
    print("Succes ...graet")
