import socket
import threading


def Client_handle(Client_socket, counter):
    while True:
        data_recv = Client_socket.recv(1024).decode()
        print(data_recv)

        data = input(f"\n {counter} > Enter text :")
        Client_socket.send(data.encode())


Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP

# 1-1024 Wellknown - you dont touch
Server_Socket.bind(('172.20.130.12',5500))
# IP | PORT { TLS- 443  | 80 }
Server_Socket.listen()
obj_clients = []
counter = 1
while True:
    print(" \n the Server is Listening....... ")
    Client_socket,IP_PORT =Server_Socket.accept()
    obj_clients.append(Client_socket)
    print(f"\n The client with IP and PORT {IP_PORT} is Connected ")
    th_client = threading.Thread(target=Client_handle, args=(Client_socket,counter))
    th_client.start()
    counter +=1

