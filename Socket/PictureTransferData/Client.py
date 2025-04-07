import socket
import os


file_name = input(" Enter The name file :")
file_size = os.stat(file_name)
file_size = file_size.st_size

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect(('172.20.150.178',6600))

with open(file_name, "rb") as file:
    data = file.read()
Client_socket.send(file_name.encode()) # Name
Client_socket.send(str(file_size).encode()) #Size
Client_socket.send(data) # BinaryData

