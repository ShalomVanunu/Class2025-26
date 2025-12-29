import socket
import pickle
import json

json1 = { "Name" : "Data", "Age":[17,18]}
json_data = json.dumps(json1)
json_bin = pickle.dumps(json1)


Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.155.118',5500))

Client_socket.send(json_data.encode())

print(Client_socket.recv(1024).decode())