import socket


Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP

# 1-1024 Wellknown - you dont touch
Server_Socket.bind(('172.20.150.178',6600))
# IP | PORT { TLS- 443  | 80 }
Server_Socket.listen()
print(" the Server is Listening....... ")
Client_socket,IP_PORT =Server_Socket.accept()
print(Client_socket)
print(f" The client with IP and PORT {IP_PORT} is Connected ")

file_name = Client_socket.recv(1024).decode()
file_size = Client_socket.recv(1024).decode()
file_data = Client_socket.recv(int(file_size))
NewName = file_name.split(".")[0]+"New"
file_name = NewName+"."+file_name.split(".")[1]
with open(file_name, "wb") as file:
     file.write(file_data)



