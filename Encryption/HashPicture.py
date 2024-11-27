import hashlib

with open("cat.jpg","rb" ) as file :
    file_cont = file.read()

hash_MD5 = hashlib.md5(file_cont).hexdigest()
print(hash_MD5)

with open("cat1.jpg","rb" ) as file :
    file_cont = file.read()
hash_MD5 = hashlib.md5(file_cont).hexdigest()
print(hash_MD5)