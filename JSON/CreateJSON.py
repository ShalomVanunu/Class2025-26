
import json

# יצירת נתוני JSON
data = {"name": "David", "age": 17, "hobbies": ["Reading","Gaming"]}
json_data = json.dumps(data, "file.txt")
print(type(json_data))


name = "shalom"
age = 25
city = "London"


person = {
    "name": name,
    "age": age,
    "city": city
}


