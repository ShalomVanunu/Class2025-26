
import requests

URL = "https://hack-yourself-first.com/"

url_content = requests.get(URL)

url_content_post = requests.post(URL,data = {'Email':'shalom@gmail.com','Password':'qweasd'})

#print(url_content_post.text)

if "Log in" not in url_content_post.text: # check Home page
    print("Success ...great")
