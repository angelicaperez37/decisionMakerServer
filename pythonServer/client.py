import socket              # Import socket module

s = socket.socket()        # Create a socket object
port = 80                # Reserve a port for your service.

s.connect(("192.168.1.85", port))
print s.recv(80)
s.close                    # Close the socket when done
