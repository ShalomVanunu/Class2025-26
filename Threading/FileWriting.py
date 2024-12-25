import threading
import os
import time
import random
import string
from time import sleep


def random_sign():
    signs = string.punctuation
    return random.choice(signs)

def file_name(i):
    return "file"+str(i)


def main():
    os.mkdir("files")
    os.chdir("files")
    for i in range(1,11):
        sign = random_sign()
        with open(file_name(i),"w") as file:
            file.write(10000*sign)
        time.sleep(1)


start = time.time()
main()

stop = time.time()
print("CT = ",stop-start)






