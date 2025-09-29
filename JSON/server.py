#!/usr/bin/env python3
"""
Server: always expects Pickle containing a JSON string.
"""

import socket
import threading
import pickle
import json
import struct

HOST = '0.0.0.0'
PORT = 65432

def recv_all(conn, n):
    """Receive exactly n bytes."""
    data = bytearray()
    while len(data) < n:
        packet = conn.recv(n - len(data))
        if not packet:
            raise ConnectionError("Connection closed while receiving data")
        data.extend(packet)
    return bytes(data)

def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    try:
        # read 4 bytes length
        raw_len = recv_all(conn, 4)
        (payload_len,) = struct.unpack('>I', raw_len)
        payload = recv_all(conn, payload_len)
        print("payload ", payload)
        try:
            # Unpickle -> JSON string
            json_string = pickle.loads(payload)
            print("json_string ",json_string)
            data = json.loads(json_string)
            print("data ",data)
            print(data["FirstName"])
            print("[*] Received data (Pickle-wrapped JSON):")
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except Exception as e:
            print("[-] Failed to decode payload:", e)

    finally:
        conn.close()
        print(f"[-] Connection closed {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT} ...")
        try:
            while True:
                conn, addr = s.accept()
                threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
        except KeyboardInterrupt:
            print("\n[!] Server shutting down.")

if __name__ == "__main__":
    main()
