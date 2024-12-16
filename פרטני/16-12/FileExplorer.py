import os

path = input("Enter teh Path : ")
os.chdir(path)
print("Current :"+os.getcwd())
#print(os.listdir())
result = os.popen("dir")
print(result.read().encode("utf-8"))
#os.system("winword")

