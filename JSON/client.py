#!/usr/bin/env python3
"""
Client: creates JSON data, then pickles the JSON string and sends it.
"""

import socket
import json
import pickle
import struct

HOST = '127.0.0.1'
PORT = 65432

def build_message(data: dict) -> bytes:
    """
    Build: 4-byte length prefix + pickled JSON string
    """
    json_string = json.dumps(data, ensure_ascii=False)
    print("json_string ",json_string)
    payload = pickle.dumps(json_string)  # pickle the JSON string
    print("payload pickle ",payload)
    length = struct.pack('>I', len(payload))
    return length + payload

def main():
    print("Enter the following details to send to the server:")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    phone = input("Phone number: ").strip()

    record = {
        "FirstName": first,
        "LastName": last,
        "Phone": phone
    }

    msg = build_message(record)

    try:
        with socket.create_connection((HOST, PORT)) as sock:
            sock.sendall(msg)
            print(f"[+] Sent {len(msg)} bytes (Pickle-wrapped JSON) to {HOST}:{PORT}")
    except Exception as e:
        print("[-] Failed to send message:", e)

if __name__ == "__main__":
    main()
