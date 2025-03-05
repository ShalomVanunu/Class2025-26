import tkinter as tk
import socket
import threading

Client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client_socket.connect(('172.20.131.190',3434))

def Send_data():
    Client_socket.send(entry.get().encode())

def recv_data():
    while True:
        data =Client_socket.recv(1024).decode()
        text_box.insert(tk.END, "Server :"+data+"\n")

th = threading.Thread(target=recv_data)
th.start()


root = tk.Tk()

root.title("Client Chat Window")
root.configure(background='blue')

text_box = tk.Text(root,height=10, width=50)
text_box.pack()

entry = tk.Entry(root, width=40)
entry.pack(side =tk.LEFT,pady = 10, padx = 10)

send_button = tk.Button(root,text='SEND',command=Send_data)
send_button.pack(side =tk.LEFT)





root.mainloop()





