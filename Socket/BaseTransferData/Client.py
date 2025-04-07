import socket



Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.153.213',5423))

Client_socket.send("Hello".encode())

print(Client_socket.recv(1024).decode())