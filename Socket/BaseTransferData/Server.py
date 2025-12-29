import socket
import pickle
import json

Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP

# 1-1024 Wellknown - you dont touch
Server_Socket.bind(('172.20.155.118',5500))
# IP | PORT { TLS- 443  | 80 }
Server_Socket.listen()
print(" the Server is Listening....... ")
Client_socket,IP_PORT = Server_Socket.accept()
print(Client_socket)
print(f" The client with IP and PORT {IP_PORT} is Connected ")

data_recv = Client_socket.recv(1024)
print(json.loads(data_recv.decode()))


