import socket

Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP

Server_Socket.bind(('172.20.153.213',5423))
# IP | PORT { TLS- 443  | 80 }
Server_Socket.listen()
print(" the Server is Listening....... ")
Client_socket,IP_PORT =Server_Socket.accept()
print(f" The client with IP and PORT {IP_PORT} is Connected ")

data_recv = Client_socket.recv(1024).decode()
print(data_recv)

Client_socket.send("Got data".encode())


