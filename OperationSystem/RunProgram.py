import os

os.system("calc.exe")

run_resault = os.popen("systeminfo")

print(run_resault.read())



