import socket

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('84.229.34.63',5050))

Client_socket.send("Hello".encode())

print(Client_socket.recv(1024).decode())