import socket              # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
port = 8080                # Reserve a port for your service.

s.connect(("192.168.1.85", port))
#s.send("swing")
while(1):
    data = s.recv(8080)
    if data == 'q' or data == 'Q':
        s.close()
        break
    elif data != '':
        print 'Received: ' + data

s.close                    # Close the socket when done
