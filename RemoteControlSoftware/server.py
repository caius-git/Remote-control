#!/usr/bin/env python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.7", 6666))
listener.listen(0)
print("[+] Listening for connections")
listener.accept()
print("[+] Connection established with target")

