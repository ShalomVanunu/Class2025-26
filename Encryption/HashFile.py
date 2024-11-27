import hashlib

with open("MaltegoSetup.JRE64.v4.8.1.exe","rb" ) as file :
    file_cont = file.read()

# 19787fd4beb417e55c740df8cea3df4a

hash_MD5 = hashlib.md5(file_cont).hexdigest()
print(hash_MD5)
