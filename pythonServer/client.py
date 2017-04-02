import socket              # Import socket module
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
port = 8080                # Reserve a port for your service.

s.connect(("192.168.1.85", port))
#s.send("swing")
#while(1):
s.sendall("swing")
print s.recv(8080)

f = open('torecv.png','wb')
'''while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
    print "Done Receiving"
'''
s.close                    # Close the socket when done
