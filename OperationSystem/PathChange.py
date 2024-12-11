import os


#os.mkdir("..")
os.chdir("New")
path = os.getcwd()
path.split("\\")
new_path = "\\".join(path.split("\\")[0:2])
print(new_path)
#with open("new.txt", "w") as file:
 #   file.write("Hello class")

os.chdir("..")
print(os.getcwd())