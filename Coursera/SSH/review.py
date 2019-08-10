# Interfacing with the Raspberry Pi
# Module 2 Assignment - Simple Web Server

# Import the libraries
import socket
import sys

# Create the server socket
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("ERROR: Failed to create server socket")
    sys.exit()

# Bind the server socket to port 80
try:
    serversocket.bind(('', 80))
except socket.error:
    print('ERROR: Failed to bind server socket')
    sys.exit()

# Listen for an incoming connection from a client
serversocket.listen(1)

# Accept the incomming connection 
conn, addr = serversocket.accept()
print("Connection accepted from:", addr[0], '\n')

# Receive data from the buffer
data = conn.recv(1024)
print('Request received:', data, '\n')

# Send a response to the client
response = b'<!DOCTYPE html><html><body><H1>Raspberry Pi Web Server</H1></body></html>'
conn.sendall(response)
print('Response sent:', response, '\n')

# Close the connection 
conn.close()
print('Connection closed\n')

# Close the socket
serversocket.close()
