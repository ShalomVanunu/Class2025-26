import hashlib

plain_text = b"Cyber"

hash_MD5 = hashlib.sha256(plain_text).hexdigest()

print(hash_MD5)
