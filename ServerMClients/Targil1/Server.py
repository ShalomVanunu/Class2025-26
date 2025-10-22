import socket
import threading



def Client_handle(Client_socket):

    while True:
        data_recv = Client_socket.recv(1024).decode()
        print(clients[Client_socket], data_recv)
        data = "ACK"
        Client_socket.send(data.encode())

Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP
user_names = []
# 1-1024 Wellknown - you dont touch
Server_Socket.bind(('172.20.130.12',5500))
# IP | PORT { TLS- 443  | 80 }
(Server_Socket.listen())
clients = {}
print(" the Server is Listening....... ")

while True:
    Client_socket,IP_PORT =Server_Socket.accept()
    user_name = Client_socket.recv(1024).decode()
    Client_socket.send("Welcome to Server".encode())
    clients[Client_socket] = user_name
    print(f" The client with IP and PORT {IP_PORT} is Connected ")

    th_client = threading.Thread(target=Client_handle, args=(Client_socket,))
    th_client.start()