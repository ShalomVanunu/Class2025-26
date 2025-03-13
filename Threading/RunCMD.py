import os
import  threading

commands = ['systeminfo', 'whoami', 'ipconfig', 'netstat']


def run_cmd(command):
     print(os.popen(command).read())
#
# for command in commands:
#     th = threading.Thread(target=run_cmd , args=(command,))
#     th.start()
list_th = []

for command in commands:
    th = threading.Thread(target=run_cmd , args=(command,))
    list_th.append(th)

for th in list_th:
    th.start()
    th.join()