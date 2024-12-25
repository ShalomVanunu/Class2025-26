import os
import threading
import time



def run_cmd(command):
    result = os.popen(command).read()
    print(result)

start= time.time()
list_cmd = ['systeminfo', 'whoami','ipconfig']
for cmd in list_cmd:
    th = threading.Thread(target=run_cmd, args=(cmd,))
    th.start()


print('\033[35m'+"All time ",time.time()-start)
