import socket



Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.130.12',5500))

user_name = input(" Enter your Username :")
Client_socket.send(user_name.encode())
print(Client_socket.recv(1024).decode())
while True:
    data = input(" Enter Message :")
    Client_socket.send(data.encode())
    print(Client_socket.recv(1024).decode())