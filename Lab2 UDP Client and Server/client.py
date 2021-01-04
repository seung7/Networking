from socket import *
#import socket
import time
count=10
pingcount=0

#127.0.0.1 is localhost
serverName = '127.0.0.1' 
serverPort = 12000

#creating the client's socket, called client socket
#AF_INET means using IPv4.
#SOCK_DGRAM means using UDP socket.
#socket.clientSocket = socket(socket.AF_INET,socket.SOCK_DGRAM) 
clientSocket = socket(AF_INET,SOCK_DGRAM) 
print("this is clinet")

#if not getting responds within 1 second, it gets timeout and call 'except'
clientSocket.settimeout(1)

while count>0 :
    #measure the current time
    #message.encode() converts string type to byte type
    #sendto have destination address to the message.
    initial_time= str(time.time()) 
    clientSocket.sendto(initial_time.encode(),(serverName, serverPort))
    

    #printout the pingnumber
    pingcount+=1
    print("pingcount:",pingcount)
    
    try:
        #when a packet arrives from internet, it get saved at modifiedMessage.
        #serverAddress has server's IP address and portnumber.
        #2048 is the buffer size
        #decoded_Message converts type byte to type string
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        decoded_Message = modifiedMessage.decode()
        
        #RTT_time is calculated by subtracting current time by initial_time
        RTT_time =  time.time()-float(decoded_Message)
    
        print("One RTT took : ", RTT_time, "seconds")
    except:
        print("request timed out")
    
    count -=1

clientSocket.close()




