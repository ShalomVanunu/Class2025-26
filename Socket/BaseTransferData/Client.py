import socket
import pickle

json = { "Name" : "Data", "Age":[17,18]}
json_bin = pickle.dumps(json)
print(json)
print(json_bin)

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.155.118',5500))

Client_socket.send(json_bin)

print(Client_socket.recv(1024).decode())