import socket

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.130.12',5500))

while True:
    Client_socket.send("Client got Data".encode())

    print(Client_socket.recv(1024).decode())
