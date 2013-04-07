#Client Side

import sys
#for Sockets
import socket
#for time stamp
import time

user_name = input("User Name: ")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print ('Failed to create socket. Error code: ' + str(msg[0]) + ', Error message : ' + msg[1])
    sys.exit();

host = '127.0.0.1'
port = 8888

s.connect((host, port))

print ('Socket connected to ' + host)

while True:
    
    action = input("Action? answer|comment|question: ")
    if action == 'answer' or action == 'comment' or action == 'question': 
        content = input ("Content: ")
        confirm = input ("confirm to submit " + action + "[Y/N] ")
        while (confirm != 'N' and confirm != 'Y'):
            print("please type Y/N")
            confirm = input ("confirm to submit " + action + "[Y/N] ")
        if confirm == 'N' or confirm == 'n':
            print("Cancelled")
            continue
        elif confirm == 'Y' or confirm == 'y':
            cur_time = int (time.time())
            request = '{"time":'+str(cur_time)+',"user":"'+user_name+'","action":"'+action+'","content":"'+content+'"}'
            try:
                print(request)
                s.sendall(request.encode('utf-8'))
            except socket.error:
                print ("Send failed")
                sys.exit()
            print("Message Sent")
    else:
        print("please type correct action")


            
    
    
