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


def main(i):
        sign = random_sign()
        with open(file_name(i),"w") as file:
            file.write(10000*sign)
        time.sleep(1)

try:
    os.mkdir("files")
except:
    print(" the folder files exist")

os.chdir("files")
start = time.time()
th_list = []
for i in range(1,11):
    th = threading.Thread(target=main, args=(i,))
    th_list.append(th)
    th.start()


print(th_list)

for th in th_list:
    th.join()

stop = time.time()
print("CT = ", stop - start)








