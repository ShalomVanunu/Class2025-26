
import json

name = "shalom"
age = 25
city = "London"


person = {
    "name": name,
    "age": age,
    "city": city
}


with open("JSONExample","w") as file:
    json.dump(person,file,indent=4)

