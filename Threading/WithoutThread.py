import time

start = time.time()
print('\033[31m'+ "Number 1")
time.sleep(3)
print('\033[32m'+ "Number 2")
print('\033[34m'+ "Number 3")

print('\033[35m'+"All time ",time.time()-start)
