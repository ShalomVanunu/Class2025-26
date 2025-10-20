import socket
import threading

import Threading

def Client_handle(Client_socket, Clients):
    while True:
        data_recv = Client_socket.recv(1024).decode()
        print(data_recv)

        data = input("Enter text :")
        for obj_client  in Clients: # Clients is the list of obt clients
            obj_client.send(data.encode())


Server_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = IPv4 || SOCK_STREAM - TCP

# 1-1024 Wellknown - you dont touch
Server_Socket.bind(('172.20.130.12',5500))
# IP | PORT { TLS- 443  | 80 }
Server_Socket.listen()
obj_clients = []

while True:
    print(" the Server is Listening....... ")
    Client_socket,IP_PORT =Server_Socket.accept()
    obj_clients.append(Client_socket)
    print(f" The client with IP and PORT {IP_PORT} is Connected ")
    th_client = threading.Thread(target=Client_handle, args=(Client_socket,obj_clients))
    th_client.start()

