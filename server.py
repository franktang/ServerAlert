#Server Side

import sys
# for sockets
import socket
import spamCheck
from _thread import *


HOST = ''
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

s.listen(10)
print ('Socket now listening')

def clientThread(conn):
    list = []
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if not data:
            break
        print ("Request Received: " + str(data))
        data = eval(data)
        spamCheck.evaluate(data, list)
        list.append(data)    
    conn.close()


while True:
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(clientThread,(conn,))
    
s.close()



