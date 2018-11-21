"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Seven

This is the client for a simple message echo program.

"""
import socket

# Initialize Variables
HOST = socket.gethostname()
PORT = 55555
MESSAGE = "Demo Message - client: Hunter Carlisle"
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except socket.error as e:
    print(str(e))

s.send(str.encode(MESSAGE))

data = s.recv(BUFFER_SIZE)

s.close()
print('Received', repr(data))


""" PROGRAM RUN: CLIENT
Received b'Demo Message - client: Hunter Carlisle'

Process finished with exit code 0
"""