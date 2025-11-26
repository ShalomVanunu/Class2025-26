import socket
import time
import threading
import random

"""
Connects to the server and stays connected for a random amount of time.
"""
SERVER_IP = '172.20.155.118'
SERVER_PORT = 9000      # Port for raw TCP clients

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print(f"[Client  Connected to server.")

# Send a heartbeat or data occasionally
while True:
    msg = input("Enter a message :")
    client.send(msg.encode())
    data = client.recv(1024).decode()
    print("Data recieve :",data)

