import socket
import threading
from flask import Flask, render_template_string,render_template

# --- Global State ---
# We use a set to store unique IPs, or a list if you want to see duplicate connections from same IP.
# Using a list here to show specific connection instances.
connected_clients = []

# Configuration
TCP_IP = '172.20.155.118'
TCP_PORT = 9000      # Port for raw TCP clients
WEB_PORT = 6060      # Port for Flask Dashboard


def handle_client(client_socket, client_address):
    """
    Handles a single client connection in a separate thread.
    Waits for the client to disconnect.
    """
    global connected_clients

    ip, port = client_address
    client_info = {'ip': ip, 'port': port}

    # Add to global list
    print(f"[NEW CONNECTION] {ip}:{port} connected.")
    connected_clients.append(client_info)


    while True:
        # We assume a simple keep-alive or echo server.
        # If recv returns 0 bytes, the client closed the connection.
        msg = client_socket.recv(1024).decode()
        print(msg)
        if not msg:
            break
        data = input("Write message :")
        client_socket.send(data.encode())


            # Optional: Echo back to client or process data
            # client_socket.send(b"Server received: " + msg)


def socket_layer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (ip v4) SOCK_STREAM - TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((TCP_IP, TCP_PORT))
    server_socket.listen()
    while True:
        # Accept new connection
        conn, addr = server_socket.accept()

        # Spin up a new thread for this client so the main loop isn't blocked
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True  # Thread dies if main program dies
        thread.start()



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", clients=connected_clients, tcp_port=TCP_PORT, web_port=WEB_PORT)


socket_th = threading.Thread(target=socket_layer)
socket_th.start()

app.run(host=TCP_IP, port=WEB_PORT, debug=False)