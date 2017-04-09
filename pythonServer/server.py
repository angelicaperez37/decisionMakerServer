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
    sleep(20)
    call(['raspistill', '-e', 'png','-ss', '10000', '-o', '/tmp/result.png'])
    return '/tmp/result.png'

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

    #Initialize servo
    servo.init()

    #now keep talking with the client
    while 1:
        #Start listening
        s.listen(PORT)
        print 'Socket now listening.'
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        #conn.send("Hello")
        data = conn.recv(PORT)
        if data == 'q' or data == 'Q':
            s.close()
            break
        elif data == 'swing':
            print 'Received: ' + data
            filePath = swing()
            f = open(filePath,'rb')
            print 'Sending...'
            l = f.read(4096)
            while (l):
                conn.send(l)
                l = f.read(4096)
	    conn.send("END_OF_FILE")
            print 'Done sending.'

main([])
