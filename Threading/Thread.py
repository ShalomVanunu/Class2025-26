import time
import threading



start = time.time()
def print_num():
    print('\033[31m'+ "Number 1")
    time.sleep(3)
    print('\033[32m'+ "Number 2")
    print('\033[34m'+ "Number 3")

th = threading.Thread(target=print_num)
th.start() # start the Thread
#th.join() # continue just after the thread ended

print('\033[33m'+ "Number 4")
print('\033[35m'+"All time ",time.time()-start)
