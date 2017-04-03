'''
    Simple socket server using threads
'''

import socket
import sys
import servo
from time import sleep
from subprocess import call

def swing():
    servo.swing()
    sleep(40)
    call(['raspistill', '-e', 'png', '-o', 'images/result.png'])
    return 'images/result.png'

def main(args):

    HOST = ''   # Symbolic name, meaning all available interfaces
    PORT = 8080 # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print 'Socket bind complete'

    #Start listening on socket
    s.listen(8080)
    print 'Socket now listening'

    #Initialize servo
    servo.init()

    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        #conn.send("Hello")
        data = conn.recv(8080)
        if data == 'q' or data == 'Q':
            s.close()
            break
        elif data == 'swing':
            print 'Received: ' + data
            filePath = swing()
            f = open(filePath,'rb')
            print 'Sending...'
            l = f.read(1024)
            while (l):
                print 'Sending...'
                conn.send(l)
                l = f.read(1024)
           # s.close()
           # break

    #s.close()

main([])
