import requests

url_pic= "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759"

url_cont= requests.get(url_pic).content
with open("picture1.jpg","wb") as file:
    file.write(url_cont)

