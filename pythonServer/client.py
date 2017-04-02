import socket              # Import socket module
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
port = 8080                # Reserve a port for your service.

s.connect(("192.168.1.85", port))
#s.send("swing")
#while(1):
s.sendall("swing")
data_received = s.recv(8080)

f = open('img.jpg','wb')
f.write(data_received)
f.close()

print "Done Receiving"

s.close                    # Close the socket when done
