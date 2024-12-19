import os
from os.path import exists

try:
    os.mkdir("Shalom")
except:
    print("there is a problem!")

os.mkdir("Shalom", exist_ok=True)
os.chdir("Shalom")
file = open("text.txt", "w")
file.write("Hello")
file.close()

