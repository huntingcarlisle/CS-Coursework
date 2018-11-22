"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Seven

This is the server for a simple message echo program.
"""

import socket

HOST = socket.gethostname()
PORT = 55555
BUFFER_SIZE = 1024
LISTEN_BACKLOG = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

s.listen(LISTEN_BACKLOG)
print("Waiting for Connection...")

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    conn.send(data)

conn.close()
s.close()

""" PROGRAM RUN: SERVER
Waiting for Connection...
Connected by ('192.168.1.4', 62078)

Process finished with exit code 0
"""