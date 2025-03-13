from tkinter import *
import os
import threading

list_ips = []

def check_ip(ip):
    global list_ips
    result = os.popen(f"ping -n 1 {ip}").read()
    if "TTL" in result:
        list_ips.append(ip)
        text_box.insert(END,ip+"\n")

def scan_lan():
    start_ip = entry1.get()
    stop_ip = entry2.get()

    network_id = ".".join(start_ip.split(".")[:3])
    start_byte = int(start_ip.split(".")[3])
    stop_byte = int(stop_ip.split(".")[3])

    for last_byte in range(start_byte,stop_byte+1):
        ip = network_id+"."+str(last_byte)
        th = threading.Thread(target=check_ip, args=(ip,))
        th.start()


def save_file():
    with open("list_ips","w") as file:
            file.write("\n".join(list_ips))

app = Tk() # app object from Tkinter
app.title("Scan LAN")
app.geometry("300x300")
app.resizable(False,False)

label1  = Label(app, text = "Start IP")
label1.pack()
entry1 = Entry(app,)
entry1.pack()

label2  = Label(app, text = "Stop IP")
label2.pack()
entry2 = Entry(app,)
entry2.pack()

button1 = Button(app, text = "Scan!",command=scan_lan)
button1.pack()
button2 = Button(app, text = "Save", command=save_file)
button2.pack()

text_box = Text()
text_box.pack()

app.mainloop() #  run the tKINTER OBJECT