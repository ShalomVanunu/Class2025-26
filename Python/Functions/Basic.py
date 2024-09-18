import time


def calc(num1,num2):
    #print(num1+num2)
    return num1+num2

def show_time():
    print(time.time_ns())

num1 =3
num2 =5
print(calc(num1,num2))
show_time()


